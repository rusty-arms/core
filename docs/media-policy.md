# Media policy

Source: [research brief](research/brief.md) §8.

| Media | Rule |
|---|---|
| Original models, textures, animations, audio, fonts, scripts, data | Load from the player's disc at runtime. Never commit or ship them. |
| Movies (Bink, on the disc) | Decode at runtime with FFmpeg's open Bink decoder. Never ship them. |
| HD textures, upscaled movies | Ship the recipe (script, model and settings). Each player generates their own copies. |
| Rips from websites, Steam Workshop or the community HD pack | Never use them. Being public does not make them licensed. |
| Fan art made from scratch | Allowed with the artist's written licence, unless it depicts Glitch or other named characters. |
| The engine's own media (menus, icons, logo, test placeholders) | Original, or openly licensed (CC0 assets, OFL fonts). |
| New missions (Phase 5) | May reference original enemies, props and textures by name, loaded from the disc. New characters, music and voices must be original. No AI clones of the original voice cast. |

## Notes

- **HD texture recipe:** upscale with chaiNNer and a CC0 model trained on 2000s game textures, such as 4x-PBRify_UpscalerV4, with human review. Publish the model name, licence, settings and a script each player runs on their own disc. Label AI-processed content.
- **Screenshots and captures of the game** are never committed to any repo, including for bug reports or docs. They belong in the lab.
- **Content tools:** do not use Hunyuan3D (its licence excludes the UK). TRELLIS.2 is MIT-licensed but its output needs retopology. Keep BlenderMCP on localhost.
