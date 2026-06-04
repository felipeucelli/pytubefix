# How to Contribute to Pytubefix

## Development Workflow

Pytubefix follows a development-first workflow.

All development work must be based on the `dev` branch.

Contributors should:

1. Fork the repository.
2. Create a feature or fix branch from `dev`.
3. Commit and test their changes.
4. Submit a Pull Request targeting the `dev` branch.

Pull Requests opened against `main` may be closed and contributors will be asked to resubmit them against `dev`.

## Commit Signing Requirement

All commits must be signed off using the Developer Certificate of Origin (DCO).

Pull Requests containing one or more commits without a valid `Signed-off-by` line will be rejected.

The easiest way to create compliant commits is:

```bash
git commit -s
```

This automatically appends:

```text
Signed-off-by: Your Name <your.email@example.com>
```

## Did You Find a Bug?

* Ensure the bug was not already reported by searching GitHub Issues.

* If you're unable to find an existing issue, open a new one and include:
  * A clear title and description.
  * Relevant environment information.
  * A Minimal Reproducible Example (MRE) or executable test case.

* For more detailed information on submitting bug reports, see: `TODO`.

## Did You Write a Patch That Fixes a Bug?

* Open a Pull Request against the `dev` branch.

* Ensure the PR description clearly explains:
  * The problem.
  * The solution.
  * Any related issue numbers.

* Before submitting, please read the NumPy Contribution Guidelines to learn more about coding conventions and testing practices.

## AI-Assisted Contributions

When AI tools contribute to Pytubefix development, proper attribution helps track the evolving role of AI in the development process.

Contributions developed with the assistance of AI tools must include an `Assisted-by` tag in the commit message.

### Assisted-by Format

```text
Assisted-by: AGENT_NAME:MODEL_VERSION [TOOL1] [TOOL2]
```

Examples:

```text
Assisted-by: ChatGPT:GPT-5.5 [OpenAI]
```

```text
Assisted-by: Claude:Opus-4 [Anthropic]
```

```text
Assisted-by: GitHub Copilot:GPT-5 [GitHub] [OpenAI]
```

The `Assisted-by` tag should appear between the contributor's `Signed-off-by` lines.

Example:

```text
Improve cipher validation logic

Signed-off-by: John Doe <john@example.com>

Assisted-by: ChatGPT:GPT-5.5 [OpenAI]

Signed-off-by: John Doe <john@example.com>
```

By including a `Signed-off-by` line, contributors certify that they have reviewed the code, understand the submitted changes, and accept full responsibility for the contribution, regardless of any AI assistance used during development.

## Cosmetic Changes

Changes that are purely cosmetic and do not improve functionality, stability, maintainability, documentation quality, or testability are generally not accepted.

Pytubefix follows PEP 8 formatting standards.

## Do You Intend to Add a New Feature?

* Open an issue using the `enhancement` label before starting implementation.

* Pytubefix uses GitHub Issues not only for bug reports, but also for discussing design proposals and feature ideas.

## Do You Have Questions About the Source Code?

Ask questions about Pytubefix usage on Stack Overflow:

https://stackoverflow.com/questions/tagged/pytubefix

## Do You Want to Improve the Documentation?

Documentation contributions are always welcome.

Please consider submitting a patch to:

https://github.com/JuanBindez/pytubefix/tree/main/docs

## Final Notes

Pytubefix is a volunteer-driven project. Contributions of all sizes are appreciated.

Thank you for helping improve Pytubefix.

Pytubefix Team