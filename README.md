# URL-Scanner
A very simple but very terrible python tool to find all links on a webpage, and all links on those links, etc.

# Dependencies
This python tool (probably) requires python 3.
You will also need BeautifulSoup 4

# Supported Operating Systems
Only tested on MacOS, probably will work on Linux, and good luck Windows users.

# Arguments
python3 scrape.py [URL]

[URL] -> Target URL to scrape (No quotation marks)

# WARNING
May take upwards of 3 minutes to run, and may hang. If the program gets stuck processing a URL for more than ten seconds, press control+c.

# Output

The program outputs a list of URLS detected, and is NOT formatted. Maybe I will implement a less messy way of outputting the URLs.

# Example Output

```['', 'https://docs.github.com/site-policy/github-terms/github-terms-of-service', 'https://resources.github.com', '/features/security/software-supply-chain', 'https://github.careers', 'https://github.com/github/roadmap', 'https://github.com/features/actions', 'https://github.com/customer-stories/figma', '/features/copilot', 'https://docs.github.com/get-started/exploring-integrations/about-building-integrations', 'https://github.blog', '/solutions/industry', '/sitemap', 'https://support.github.com?tags=dotcom-footer', 'https://github.com/topics', 'https://github.com/features/code-review', 'https://x.com/github', 'https://docs.github.com/site-policy/privacy-policies/github-privacy-statement', 'https://cli.github.com', '#hero', 'https://github.com/team', 'https://www.youtube.com/github', '/solutions/industry/financial-services', '/sponsors', 'https://github.blog/news-insights/research/survey-ai-wave-grows/', 'https://github.com/features/codespaces', 'https://docs.github.com/en/code-security/code-scanning/managing-your-code-scanning-configuration/codeql-query-suites', 'https://docs.github.com/search-github/github-code-search/understanding-github-code-search-syntax', 'https://resources.github.com/devops/tools/compare', 'https://github.com/features', 'https://github.com/pricing', '/signup?ref_cta=Sign+up&ref_loc=header+logged+out&ref_page=%2F&source=header-home', 'https://github.community', '/about/diversity', 'https://services.github.com', 'https://desktop.github.com', '/features/security/code', '/features/code-review', 'https://github.com/customer-stories/mercedes-benz', 'https://github.com/enterprise/startups', 'https://github.com/customer-stories', 'https://socialimpact.github.com', '/resources/articles/ai', 'https://www.instagram.com/github', 'https://github.com/features/discussions', 'https://skills.github.com', '/enterprise/advanced-security', '/solutions/use-case/ci-cd', '/features/actions', '/solutions/industry/healthcare', 'https://github.com/features/issues', '/enterprise', 'https://github.com/readme', '/customer-stories', 'https://github.com/features/code-search', '/team', '/features/issues', '/pricing', '/newsroom', '/features/discussions', 'https://github.com/github/site-policy/pull/582', '/login', 'https://github.com/github', 'https://shop.github.com', 'https://partner.github.com', 'https://www.githubstatus.com', '/customer-stories/duolingo', '/features', '/solutions/use-case/devsecops', '#start-of-content', 'https://resources.github.com/learn/pathways', 'https://github.com/solutions/executive-insights', 'https://github.com/about', 'https://docs.github.com', 'https://www.linkedin.com/company/github', 'https://www.gartner.com/doc/reprints?id=1-2IKO4MPE&ct=240819&st=sb', 'https://www.tiktok.com/@github', '/solutions', '/enterprise/premium-support', 'https://github.com/features/copilot', '/features/codespaces', 'https://github.com/mobile', '/solutions/industry/government', 'https://github.com/enterprise/advanced-security', 'https://github.com/customer-stories/mercado-libre', '/premium-support', 'https://resources.github.com/newsletter/', 'https://github.com/features/copilot/?utm_source=github&utm_medium=banner&utm_campaign=copilotfree-bannerheader', '/resources/articles/software-development', 'https://github.com/trending', 'https://github.com/features/security', '/solutions/use-case', '/customer-stories?type=enterprise', 'https://www.twitch.tv/github', 'https://github.com/edu', 'https://github.com/enterprise', '/solutions/industry/manufacturing', '/mobile', '/git-guides', '/', '/resources/articles/security', '/security', '/readme', 'https://github.com/collections', '/features/copilot#enterprise', '/solutions/use-case/devops', '/resources/articles', '/marketplace', '/resources/articles/devops']```

# I am aware that there are LOTS of bugs. I (might) fix them. Feel free to help me :)
