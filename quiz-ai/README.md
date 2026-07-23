# Interrogazione AI — prototipo

Pagina di test: `quiz-ai/index.html` + funzione serverless `api/deepseek.js`.

## Come funziona

- Voce → testo e testo → voce girano nel browser (Web Speech API), gratis.
- `quiz-ai/index.html` manda la conversazione a `/api/deepseek`.
- `api/deepseek.js` gira su Vercel, legge la chiave da `DEEPSEEK_API_KEY`
  (variabile d'ambiente lato server) e la inoltra a DeepSeek. La chiave non
  è mai scritta nel codice del sito.

## Deploy su Vercel (una volta sola)

1. Vai su vercel.com → New Project → importa questo repo GitHub
   (`infononservesaperlo-boop/orbit_sito`).
2. Framework preset: "Other" (sito statico), build command vuoto,
   output directory: `.` — Vercel rileva da solo la cartella `api/`.
3. In Project Settings → Environment Variables aggiungi:
   `DEEPSEEK_API_KEY` = la tua chiave DeepSeek.
4. Deploy. La pagina di test sarà su `https://<tuo-progetto>.vercel.app/quiz-ai/`.

Il sito principale continua a essere pubblicato su GitHub Pages come ora:
questo è un progetto Vercel separato, solo per testare la funzionalità.
Quando siete soddisfatti si potrà collegare/integrare nel sito vero.

### Trovare il link di test di questo branch

Se il branch `claude/orbit-ai-voice-quiz-x4y29m` non è quello di produzione
del progetto Vercel, ogni push su questo branch crea comunque un suo
"Preview Deployment" separato. Su vercel.com → progetto → tab
**Deployments**, cerca la riga con accanto il nome del branch
`claude/orbit-ai-voice-quiz-x4y29m` e apri il link di quella riga
(non quello in cima, che è la produzione): porta a `/quiz-ai/` di
questo stesso branch.

## Test in locale

```bash
npm i -g vercel
vercel dev
```
Poi apri `http://localhost:3000/quiz-ai/`. Serve un file `.env.local` nella
root del progetto con `DEEPSEEK_API_KEY=...` (già escluso da git).
