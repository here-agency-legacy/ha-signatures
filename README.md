# Here Agency email signatures (Nov 2026)

Current dark design, rebuilt so it stacks on phones. One signature per person.

## What we need from you

1. Upload the four images to wearehere.digital so we no longer depend on Stripo. The GIF and logo are in `preview_assets/`. Download the two social icons from the Stripo links in the HTML. Keep the same file names (emailgif.gif, herelogo.png, igemail.png, inemail.png) in one folder. Then point the `CDN` constant at that folder in `build_signatures.py` and run `python build_signatures.py .`
2. Send a test email to an iPhone and an Android phone, in the Gmail app and Apple Mail.
3. Push all six signatures with the Gmail API (Option B below), so nobody on the team has to do it by hand.
4. Host `index.html` at an unlisted URL, for example wearehere.digital/signatures. The team can use it as a backup to copy their signature.

| Person | Title | Phone | Email |
|---|---|---|---|
| Lincoln Assis | Managing Partner | 0401 495 143 | lincoln@wearehere.digital |
| Kevin Berot | Managing Partner | 0432 736 197 | kev@wearehere.digital |
| Brodie Edwards | Creative Director | none | brodie@wearehere.digital |
| Carolina Magalhaes | Project Manager | 0402 212 509 | carol@wearehere.digital |
| Lucia Baldi | Designer | none | lucia@wearehere.digital |
| Marcus Nascimento | Marketing Coordinator | 0452 460 824 | marcus@wearehere.digital |

## What's in the folder

- `index.html` shows every signature at desktop and phone width, with copy buttons.
- `signatures/*.html` has one file per person. The signature sits between the `SIGNATURE START` and `SIGNATURE END` comments.
- `signatures.json` has the same signature HTML for each person, ready for the Gmail API.
- `push_signatures.py` pushes all six to Gmail in one run.
- `preview_assets/` holds the GIF, logo and icons. They're embedded in `index.html` only, so the preview works offline. The signatures themselves always use the hosted image links, because Gmail needs them. The GIF is the original from Dropbox (Here Branding › Stationery › E-Mail signature › GIF).

## Option A: paste by hand (5 min per person)

1. Open `index.html` in Chrome.
2. Click **Copy signature** on the person's card.
3. In their Gmail, go to Settings > See all settings > General > Signature > Create new.
4. Paste. Set it as the default for new emails and for replies/forwards. Save changes at the bottom of the page.
5. Delete the old signature.

Gmail won't accept raw HTML in that box, so use **Copy signature**, not **Copy HTML source**.

## Option B: push everyone at once (Gmail API)

Setup steps are at the top of `push_signatures.py`. You need a Workspace admin to approve domain-wide delegation with the `gmail.settings.basic` scope.

```
python push_signatures.py            # dry run
python push_signatures.py --apply    # writes all six
```

## How the responsive layout works

Gmail removes `<style>` blocks and media queries from signatures, so the layout uses only inline CSS:

- The outer table is `width="600"` with `width:100%; max-width:600px`.
- The two halves (pattern + details, logo + tagline) are `display:inline-block` divs, 340px and 260px wide.
- On screens narrower than 600px, the logo half moves under the details. No media query needed.
- Outlook for Windows doesn't support inline-block, so it always shows the stacked version at 600px wide. It stays readable.

Each signature is about 3,800 characters. Gmail's limit is 10,000.

## Before rollout

- Send a test from one account to an iPhone and an Android phone, in the Gmail app and in Apple Mail.
- The images (pattern GIF, logo, social icons) are hosted on Stripo's CDN (`pirhda.stripocdn.email`). If that Stripo account is ever closed, the images will break. To be safe, upload them to wearehere.digital, change the `CDN` constant in `build_signatures.py`, and run `python build_signatures.py .` to regenerate. Team details live in the `TEAM` list in the same file.
- The pattern GIF is 100×200, so it looks a little soft on retina screens. A 200×400 export shown at 100×200 would fix that.
