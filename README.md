# Here Agency email signatures (Nov 2026)

Current dark design, rebuilt so it stacks on phones. One signature per person.

## What we need from you

1. Send a test email to an iPhone and an Android phone, in the Gmail app and Apple Mail.
2. Push all 11 signatures with the Gmail API (Option B below), so nobody on the team has to do it by hand.
3. Host `index.html` at an unlisted URL, for example wearehere.digital/signatures. The team can use it as a backup to copy their signature.

| Person | Title | Phone | Email |
|---|---|---|---|
| Lincoln Assis | Managing Partner | 0401 495 143 | lincoln@wearehere.digital |
| Kevin Berot | Managing Partner | 0432 736 197 | kev@wearehere.digital |
| Brodie Edwards | Creative Director | none | brodie@wearehere.digital |
| Carolina Magalhaes | Project Manager | 0402 212 509 | carol@wearehere.digital |
| Lucia Baldi | Designer | none | lucia@wearehere.digital |
| Marcus Nascimento | Marketing Coordinator | 0452 460 824 | marcus@wearehere.digital |
| Do Viet Liem | Lead Web Engineer | none | liemdo@wearehere.digital |
| Ernest Pineda | Web Developer | none | ernest@wearehere.digital |
| Marbien Parel | Sr. QA Engineer | none | marbien@wearehere.digital |
| Nam Bui | Sr. UI/UX Designer | none | nam@wearehere.digital |
| Thai Thi Yen Nhi | Web Developer | none | nhi@wearehere.digital |

## What's in the folder

- `index.html` shows every signature at desktop and phone width, with copy buttons.
- `signatures/*.html` has one file per person. The signature sits between the `SIGNATURE START` and `SIGNATURE END` comments.
- `signatures.json` has the same signature HTML for each person, ready for the Gmail API.
- `push_signatures.py` pushes all 11 to Gmail in one run.
- `preview_assets/` holds the GIF, logo and icons. The signatures load them straight from this public repo (`raw.githubusercontent.com/here-agency-legacy/ha-signatures/main/preview_assets/`), so don't rename, move or delete these files, and keep the repo public. `index.html` also embeds them, so the preview works offline. The GIF is the original from Dropbox (Here Branding › Stationery › E-Mail signature › GIF).

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
python push_signatures.py --apply    # writes all 11
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
- To add or change a person, edit the `TEAM` list in `build_signatures.py`, then run `python build_signatures.py .` and commit the regenerated files.
- To move the images later (for example to S3), change the `CDN` constant in `build_signatures.py` and rebuild the same way.
- The pattern GIF is 100×200, so it looks a little soft on retina screens. A 200×400 export shown at 100×200 would fix that.
