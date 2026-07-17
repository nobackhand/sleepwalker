# Sleepwalker

A 3D puzzle game in a single HTML file. You never touch her — she sleepwalks endlessly forward across floating dream islands, and you rotate the world's gravity around her path with your mouse. Guide her to her bed across 5 dreams without letting her fall into the night or land hard enough to wake her.

**Play:** open `index.html` in a browser (needs internet once, for the Three.js CDN).

## Controls

| Input | Action |
|---|---|
| Drag ⟷ / ← → / scroll | Rotate the world's gravity |
| R | Restart the dream |
| M | Mute |
| 1–6 | Replay unlocked dreams |

## The six dreams

1. **The First Step** — gaps and your first tilt
2. **Turning in Sleep** — the path spirals away
3. **Falling Upward** — let her fall, then turn the world over
4. **The Winding Stair** — a lantern-lit helix
5. **The Way Home** — everything, and her bed at the end
6. **The Undertow** — a pendulum path that swings back on itself, and the sky crossed twice

## Notes

- Three.js r128 (UMD, CDN), everything else procedural in one file: geometry, palette, WebAudio music-box lullaby, rotation chimes.
- Soft landings only: impacts above the wake threshold end the dream.
- Each dream remembers her gentlest crossing time (shown when she reaches the bed).
- The night is alive: shooting stars, twin aurora ribbons, a dream-trail at her feet, landing dust and footsteps.
- `window.SW` exposes a debug/autopilot API (`SW.warp(n)`, `SW.auto(true)`, `SW.step(frames)`) used to verify all 5 levels are completable headlessly.

Built in one shot by Claude (Fable 5), 2026-07-16.
