# Zilchy.link – Private, Invite-Only Short Links

Zilchy.link is a fully FOSS, static, hand-curated short-link service.  
Unlike public URL shorteners, **Zilchy.link is private and invite-only** — only approved contributors may create or publish short links.  
This keeps the system clean, safe, spam-free, and highly reliable.

## Allowed Content

Zilchy.link only accepts links that are:

- Safe-for-work  
- Non-malicious  
- Lawful in both the UK and US  
- Free from tracking, scams, or harmful behaviour  

Content involving adult material, gambling, illegal services, malware, harassment, or anything unsafe will **not** be accepted.

## How to Add a New Short Link (Invite-Only)

If you have been granted contributor access, you may add or propose a new short link.  
The workflow matches the instructions displayed on the Zilchy.link generator interface.

1. Open the `urls.json` file in the repository.
2. Add a new entry in this format:
   `"abcd": "https://your-long-url-here",`
3. Commit your change with a message such as "updated urls.json"
4. Open a Pull Request or commit directly to main (depending on your permission level).
5. Once merged, your new short link becomes active automatically after deployment (usually under 60 seconds).

**Important Notes:**
- Zilchy.link is intentionally exclusive — an invite is required to publish links.
- All links are reviewed to ensure safety and reliability.
- The system is completely static and transparent: every short link is stored plainly inside urls.json.
