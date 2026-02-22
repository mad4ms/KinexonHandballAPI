# Releasing (KinexonHandballAPI)

## 1) Pre-flight
- Ensure `main` is green in CI
- Confirm version in `pyproject.toml` is updated
- Update changelog/release notes if used

## 2) Tag release
```bash
git checkout main
git pull

git tag vX.Y.Z
git push origin vX.Y.Z
```

## 3) What happens automatically
- GitHub Action `release.yml` builds `sdist` + `wheel`
- Artifacts are attached to a GitHub Release for the tag

## 4) Optional PyPI publish
If needed, publish from `dist/` manually or add a PyPI publish step in workflow.
