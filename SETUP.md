# Publish your profile README

1. Create a repo named **exactly** your username: [github.com/aidancgibbons/aidancgibbons](https://github.com/new) (repository name: `aidancgibbons`)
2. Push this folder:

```powershell
cd "c:\Projects\GIt Profile"
git init
git add .
git commit -m "Add profile README"
git branch -M main
git remote add origin https://github.com/aidancgibbons/aidancgibbons.git
git push -u origin main
```

3. Enable **Actions** in repo settings if you want visitors to add words to the cloud.

Regenerate the word cloud anytime:

```powershell
python scripts/generate_wordcloud.py
```
