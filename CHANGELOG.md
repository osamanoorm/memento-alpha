# Changelog

## 0.3.0 · 22 Nov 2026
Connections, and ready for the research circle.
- Connections: write "dinner sat?" and an older open line like "try that new sushi place" comes back as a card under it (Done / Not now). Links by topic (eating out, watching, reading, car, learning, writing, gifts, trips), not just shared words. Shows in the preview while typing. At most 5 a day; done lines never come back; "Not now" quiets a line for a month.
- Remind me: dated lines and month-tagged loans get a button that adds a real phone reminder to Calendar.
- Not right?: tap a line, then "Not right?" to copy the miss for the research group.
- Welcome note on first open: test version, use fake passwords, export weekly.
- Tests: 59 checks, including connections.

## 0.2.3 · 22 Nov 2026
- Roman Urdu money: "Ali ko 2000 diye", "Ali se 2k liye", "Ali ne 500 diye", "Ali ko 3000 dene hain", "Sara se 1500 lene hain".
- Honest currency: "$400" or "25 usd" shows as USD and is never added to rupee totals or balances.
- Test list: 52 real phrases checked before every push (tests/run.py).

## 0.2.2 · 22 Nov 2026
- Fixed: "I owe Ali 2000" and "borrowed 2000 from Ali" did nothing when sent.
- Fixed: "hello world" no longer tags "World" as a person.

## 0.2.1 · 22 Nov 2026
- Updates itself: on opening, Memento checks for a newer version and reloads if there is one, then shows "Updated to alpha x". Skips while you're typing.

## 0.2.0 · 22 Nov 2026
Focus: accept everything, master a few. Memento now speaks up only about money between people, things tied to a moment, and bringing things back.
- Switched off (lines are kept as written): splits ("/4"), budgets, currency, income, auto-threads, "held for" and message cards.
- Bills become tasks with an amount; invoices become "owes you".
- Spending is honest: "written down this week · from N lines", only confident lines count, no guessed categories, weekly card only after 3+ lines.
- Years, room and flat numbers are no longer read as money.
- Calculator stays as a quiet extra ("rent 95000 / 3").

## 0.1.2 · 22 Nov 2026
From Osama's Google Keep habits.
- Loans the way you write them: "5,000 Imran (Dec)" means Imran owes you; "gave Bilal 2000"; "took 3,000 from Ali". A month in brackets brings it back on the 1st of that month.
- Watch status: "watched F1" ticks the earlier "F1" line; "started Die My Love" marks it watching. Works for anything, not just movies.
- Car: "oil changed at 68,946 km", then later "car at 73,100 km" flags the oil change.
- Secrets: security pictures and questions, and CVV, are hidden too.
- Long numbers (account numbers, IBANs) get a Copy button.
- Titles like "F1" and "Die My Love" are no longer read as money or people.

## 0.1.1 · 21 Nov 2026
- README points to the new address (osamanoorm.github.io/memento-alpha) after moving the repo to Osama's account.

## 0.1.0 · 21 Nov 2026
First alpha, moved from the "Ink (test)" prototype.
- Renamed to Memento; header shows "Memento · alpha 0.1".
- Saves only on this device (local storage); Claude account sync removed.
- Web app manifest and icon, so it opens full screen from the iPhone home screen.
- Related-line links (↳) now survive a reload.
- Removed the fake "Open chat with held items" button.
- Hidden from search engines (noindex).
