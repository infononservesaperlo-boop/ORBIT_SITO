// Funzione serverless (Vercel) che fa da ponte verso DeepSeek.
// La chiave resta solo qui, letta da process.env.DEEPSEEK_API_KEY:
// non deve mai comparire nel codice del sito servito al browser.

module.exports = async (req, res) => {
  if (req.method !== 'POST') {
    res.status(405).json({ error: 'Metodo non consentito' });
    return;
  }

  const apiKey = process.env.DEEPSEEK_API_KEY;
  if (!apiKey) {
    res.status(500).json({ error: 'DEEPSEEK_API_KEY non configurata sul server' });
    return;
  }

  const { messages } = req.body || {};
  if (!Array.isArray(messages) || messages.length === 0) {
    res.status(400).json({ error: 'Campo "messages" mancante o vuoto' });
    return;
  }

  try {
    const upstream = await fetch('https://api.deepseek.com/chat/completions', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        Authorization: `Bearer ${apiKey}`,
      },
      body: JSON.stringify({
        model: 'deepseek-chat',
        messages,
        temperature: 0.7,
        max_tokens: 400,
      }),
    });

    if (!upstream.ok) {
      const detail = await upstream.text();
      res.status(upstream.status).json({ error: 'Errore da DeepSeek', detail });
      return;
    }

    const data = await upstream.json();
    const reply = data.choices?.[0]?.message?.content ?? '';
    res.status(200).json({ reply });
  } catch (err) {
    res.status(500).json({ error: 'Impossibile contattare DeepSeek', detail: String(err) });
  }
};
