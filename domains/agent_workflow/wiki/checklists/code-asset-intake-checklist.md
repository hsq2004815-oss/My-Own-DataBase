# Code Asset Intake Checklist

Use this checklist before adding a new code asset record to `processed/code_assets/`. Every item must be addressed.

## License & Legal

- [ ] License is clearly identified (SPDX or explicit statement in source)
- [ ] License is NOT GPL or AGPL (if it is, mark `do_not_copy_code`)
- [ ] License is NOT missing/unknown (if it is, mark `license_review_required` or `research_only`)
- [ ] License is compatible with target project's license
- [ ] Attribution requirements are documented

## Reuse Classification

- [ ] `reuse_level` is correctly assigned (direct_dependency / implementation_pattern / extractable_module / research_only)
- [ ] `reuse_policy` is correctly assigned (direct_use_allowed / adapter_required / inspiration_only / license_review_required / do_not_copy_code)
- [ ] If `reuse_level` is `extractable_module`, license explicitly allows code extraction and modification
- [ ] If `reuse_policy` is `do_not_copy_code`, the asset record explains why (GPL/AGPL, no license, proprietary)

## Technical Feasibility

- [ ] Dependencies are listed and assessed for weight/compatibility
- [ ] Windows compatibility is assessed (if target is Windows)
- [ ] Packaging impact is considered (PyInstaller, MSIX, etc.)
- [ ] Module boundaries are clear (for extractable_module)
- [ ] Adapter target is specified
- [ ] Adapter will NOT pollute the main pipeline

## Security

- [ ] No real API keys, tokens, passwords, or secrets in the asset record
- [ ] No private keys or credential files referenced
- [ ] No `.env` files or `secrets.ps1` content included
- [ ] Subprocess / shell calls are reviewed for injection risks

## Testing & Verification

- [ ] Required tests are listed
- [ ] Test strategy covers unit + integration + real environment
- [ ] Rollback plan is noted (for adapter integration)
- [ ] Real verification has been performed or is explicitly noted as pending

## Documentation Completeness

- [ ] `processed/code_assets/*.asset.json` record is complete
- [ ] `wiki/snippets/` or `wiki/adapters/` documentation exists (if applicable)
- [ ] `wiki/indexes/code-assets-global-index.md` has an entry for this capability
- [ ] Related assets are cross-linked via `related_snippets` / `related_adapters`

## Source Integrity

- [ ] Source is NOT large raw source copied verbatim into wiki or asset record
- [ ] Source description uses pseudo-code or interface shapes for risky-license code
- [ ] Source project is NOT modified in the process
- [ ] Source project is NOT run, built, or had dependencies installed
