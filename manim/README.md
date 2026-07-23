# ORBIT — animazioni Manim

Prima repo di animazioni per il blog di Orbit Ripetizioni: nessuna convenzione
preesistente, quindi questo file *è* la convenzione da seguire nelle prossime clip.

## Setup

Ambiente Python dedicato in `.venv-manim/` (nella root del repo, non committato).

```bash
source .venv-manim/bin/activate
```

Font richiesti (installati a livello di sistema, vedi sotto se manca l'ambiente):
Space Grotesk, Inter, IBM Plex Mono.

## Tema condiviso

`orbit_theme.py` contiene palette, font e helper (`hairline_ring`, `planet_dot`,
`display_text`, `body_text`, `eyebrow_text`, `safe_zone_scale`). Ogni nuova scena
importa da qui — non ridefinire i colori inline.

## Convenzione di naming

Un file per concetto: `scene_<slug-concetto>.py`, classe `PascalCase` che
descrive la scena (es. `DomandeGuida`).

## Convenzione "safe zone" (funziona sia orizzontale che verticale)

Ogni scena deve rendere bene sia in 1920x1080 che in 1080x1920 **con lo stesso
codice** (nessun ramo if/else per orientamento). Per questo il layout va
progettato dentro una "safe zone" quadrata centrata sull'origine, larga al
massimo ~4 unità Manim (`safe_zone_scale()` aiuta a rispettarla): è il vincolo
del formato verticale (frame_width ≈ 4.5 unità a 1080x1920) a decidere lo
spazio disponibile, non quello orizzontale.

## Render

```bash
# preview veloce (bassa qualità, entrambi i formati)
manim -ql --resolution "1920,1080" --fps 30 -o <nome>_1920x1080 scene_xxx.py NomeClasse
manim -ql --resolution "1080,1920" --fps 30 -o <nome>_1080x1920 scene_xxx.py NomeClasse

# render finale (qualità più alta)
manim -qh --resolution "1920,1080" --fps 30 -o <nome>_1920x1080 scene_xxx.py NomeClasse
manim -qh --resolution "1080,1920" --fps 30 -o <nome>_1080x1920 scene_xxx.py NomeClasse
```

Output grezzo in `media/` (non committato — vedi `.gitignore`). I file
definitivi da usare sul sito vanno copiati a mano in:

```
assets/video/blog/<slug-articolo>/<nome-clip>_<risoluzione>.mp4
```

`export/` in questa cartella è uno scratch locale per confrontare le anteprime
prima di promuoverle in `assets/video/`.

## Scene esistenti

| File | Scena | Concetto |
|---|---|---|
| `scene_domande_guida.py` | `DomandeGuida` | "Non si spiega, si fa emergere" |
| `scene_tre_modalita.py` | `TreModalita` | "Tre modalità, un solo metodo" |
| `scene_verifica_plausibilita.py` | `VerificaPlausibilita` | "Verifica di plausibilità" |

Ognuna dura 8–15s, nessun `MathTex`/LaTeX (non installato, non necessario:
tutto testo con `Text()` e i font del tema).
