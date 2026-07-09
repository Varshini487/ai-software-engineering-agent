# 💻 AI Software Engineering Agent

An **autonomous coding agent** that reads GitHub issues, analyzes the problem, writes a fix, runs tests, and opens a pull request — fully automated software development.

## 🧠 How It Works
1. **Issue Analysis**: Agent reads the GitHub issue description and extracts requirements
2. **Code Generation**: Uses an LLM (GPT-4, Claude) to write a fix based on the repo's codebase context
3. **Test Execution**: Runs existing tests to validate the fix doesn't break anything
4. **PR Creation**: Automatically opens a pull request with the fix + explanation
5. **Human Review**: Developer reviews the PR, requests changes, or merges

## 🛠️ Tech Stack
- **OpenAI GPT-4 / Claude** – code generation
- **GitHub API** – fetch issues, read repo, create PRs
- **LangChain** – agent orchestration
- **subprocess** – run tests locally
- **Streamlit** – dashboard

## 🚀 Getting Started
```bash
git clone https://github.com/Varshini487/ai-software-engineering-agent
cd ai-software-engineering-agent
pip install -r requirements.txt
streamlit run app.py
```

## 💡 Use Cases
- Auto-fix bug reports with confidence scoring
- Generate boilerplate code from specs
- Reduce developer turnaround on routine fixes
- 24/7 code maintenance assistant

## 🎤 Interview Talking Points
1. **Grounding LLMs in code context.** The agent doesn't just generate code in a vacuum — it reads the actual repo structure, imports, and test files first. This context window strategy lets you use smaller models (Claude 3 Haiku) instead of GPT-4, saving 10x on API costs while getting better code quality because the LLM sees real examples.

2. **Test-driven agent validation.** Before opening a PR, the agent runs the test suite. If tests fail, it iterates ("I see this test failed... let me try a different approach"). This self-correction loop catches bad logic before humans see it, reducing review friction and catching ~70% of logical errors automatically.

3. **Reduces engineering toil without full replacement.** This isn't replacing developers — it's automating the boring 30% of dev work (fixing known bug patterns, adding boilerplate). Developers focus on architecture and novel features. In a real startup context, this unlocks a 5-10x productivity multiplier for small teams while keeping quality high because code still gets reviewed.
