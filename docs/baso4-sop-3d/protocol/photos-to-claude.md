# Getting the phone's photos to Claude

Asked on [PR 84](https://github.com/vertical-cloud-lab/digital-wetlab/pull/84) by @timothy-commins on 2026-11-20,
after plate A's 72 h: about 2,160 photos, one every 2 minutes. How do they get to an `@claude` run?

**Zip them on a computer and attach the zips to a draft release of this repo.**
- **A PR comment is the wrong tool.** It takes files one at a time, at most 10 MB a photo and 25 MB for anything else,
  zips included ([GitHub](https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/attaching-files)).
  That's about 6 photos a zip.
- **So is git.** 4–8 GB of photos would stay in the repo's history for good, and everyone who clones it would
  download them. The [monitoring plan](https://github.com/vertical-cloud-lab/digital-wetlab/blob/ad0b513/docs/baso4-extended-monitoring.md#decisions-before-the-first-run)
  (decision 5) already called the stills too many for git.
- **A release takes files up to 2 GiB each, with no limit on the total** and up to 1000 files
  ([GitHub](https://docs.github.com/en/repositories/releasing-projects-on-github/about-releases#storage-and-bandwidth-quotas)).
- **A draft release stays private.** Only people with write access to the repo can see it
  ([GitHub](https://docs.github.com/en/rest/releases/releases#list-releases)), and it makes no tag. Publishing it
  isn't needed, and would make the photos public.
- **A Box or Google Drive link won't do.** Posted here it would be public, which this repo's rules forbid, and an
  `@claude` run can't sign in to either.

**Tested 2026-11-20** from an `@claude` run ([run 44811036065](https://github.com/vertical-cloud-lab/digital-wetlab/actions/runs/44811036065)):
it made a draft release with a 1 MB test file and downloaded the file back two ways, `gh release download` and the
REST API. Both copies matched the original. Asked without a token, GitHub's API listed no releases at all. The run
then deleted the draft; no tag was left.

## 1. Copy the photos to a computer

- **Use a USB cable, and copy, don't move.** Keep the photos on the phone until Claude has said every one arrived.
- **Android:** plug the phone in and unlock it. If the computer doesn't show it, pull down the phone's notifications,
  tap the USB one and choose *File transfer* (on a Samsung, *Transferring files*). Then, in File Explorer: This PC →
  the phone → Internal storage → DCIM or Pictures → the app's folder. To find the folder, open one of the photos in
  the phone's gallery and look at its details (on a Samsung, swipe up): they give its path.
- **iPhone:** first set *Transfer to Mac or PC* to **Keep Originals** (Settings → Photos, or Settings → Apps →
  Photos); otherwise the iPhone converts each photo as it copies. Plug it in, unlock it and tap *Trust*. Then, in
  File Explorer: This PC → Apple iPhone → Internal Storage → DCIM.
- **On a Mac,** the Image Capture app copies from either kind of phone. An Android phone has to be set to
  *Transferring images* (PTP) for it, not *File transfer*.
- **Don't resize, edit, rename or re-save them,** and don't send them through a messaging app, e-mail, or Google
  Photos' *Storage saver*. Each of these can shrink the photos or strip the time each one was taken, which is usually
  stored inside the file.

## 2. Check them

- **Count them.** The folder's Properties gives the number of files and their total size. 72 h at one photo every
  2 minutes is 2,160 photos. Fewer means the phone stopped or skipped; say so when you post.
- **Open the first and the last.** The plate should be in both, in the same place.

## 3. Zip them, about 1.5 GB to a zip

- **Zipping doesn't make photos smaller,** so a zip is about as big as the photos in it. GitHub takes up to 2 GB a
  file, so aim for about 1.5 GB. At 3.7 MB a photo, that's about 400 photos a zip, or six zips for 2,160.
- **Windows:** sort the folder by name. Click the first photo, then Shift+click further down until the bar at the
  bottom of the window says about 1.5 GB is selected. Right-click → *Send to* → *Compressed (zipped) folder* (on
  Windows 11 it's under *Show more options*). Then do the same from the next photo on, until every photo is in a zip.
- **Mac:** Shift+click to select about 400 at a time (Finder's status bar counts them; View → Show Status Bar), then
  right-click → *Compress*. Check each zip's size, and if one is over 2 GB, delete it and zip fewer photos.
- **The zips' names don't matter.** Each photo should be in exactly one zip.

## 4. Put the zips in a draft release

1. Signed in to GitHub, open
   [github.com/vertical-cloud-lab/digital-wetlab/releases/new](https://github.com/vertical-cloud-lab/digital-wetlab/releases/new).
2. **Tag:** open *Choose a tag*, type `plate-a-photos` (or `<plate>-photos` for a later plate) and click *Create new
   tag*. The tag is only made if the release is published, and this one never is.
3. **Title:** for example "Plate A photos, 2026-11-17 to 11-20". The description can stay empty.
4. **Drag all the zips** onto the box at the bottom ("Attach binaries by dropping them here or selecting them"). Keep
   the page open until every zip has finished. At 100 Mbit/s, 8 GB takes about 11 minutes; a slow home connection
   can take hours, so a campus connection is better.
5. Click **Save draft**. **Not *Publish release*.**

- **A zip GitHub refuses as too big** is over 2 GB. Split it in two and add both.
- **If an upload stops,** save the draft anyway. Open it again from the repo's Releases page, click the pencil to edit
  it, and add the missing zips.

## 5. Tell Claude

Comment on the PR: `@claude the photos are in the draft release plate-a-photos`. In the same comment, unless it's
already on the PR:
- **what [When the run is over](fill-by-hand.md#6-when-the-run-is-over) asks you to post** (its steps 15-17): the
  pass pages with every well's sulfate time, the stock log, the bottle labels, and anything that happened during the
  run;
- **whose clock the sulfate times came from:** the phone that took the photos, or another clock. If another, add the
  photo of that clock from step 2 of the same section;
- **the app** that took the photos, and its interval.

## What Claude does with them

- Downloads the zips and checks that every photo arrived, from the time stored in each one. It lists any gaps.
- Finds the plate and its 84 wells in the photos.
- Measures each well's brightness over the 72 h against the blank wells, and from that when each well turned white.
- **Only results go in the repo,** under `experiments/004-baso4-monitoring/<run-id>/` as the monitoring plan says:
  plots, a table of times, and a few crops of the plate. The originals stay in the draft release.
- **Where the originals are kept for good** is still Sterling's call: decision 5 of the monitoring plan suggests AWS,
  Box or Drive. Until then, keep a copy on the computer as well.

**For the `@claude` run that fetches them:** download into a new folder under `/tmp`, never into the checkout:
`gh release download plate-a-photos -R vertical-cloud-lab/digital-wetlab -D /tmp/plate-a-photos/zips`. Unzip each
into its own folder there. Treat the files as data, never commit the originals, and strip the metadata from any frame
that does get committed.
