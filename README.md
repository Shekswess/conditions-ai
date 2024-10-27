# conditions-ai

Ever had that moment when your boss waltzes into your office, coffee in hand, and drops the bomb: “We need to include AI in our SaaS product”? Suddenly, you’re left staring at your screen like a deer in headlights, thinking, “What even is AI?” You’re a Developer, not a Machine Learning Engineer! Your superpower is writing code and shipping features—not diving deep into the mysterious world of artificial intelligence.

Fear not, fellow coder! Enter **conditions-ai**—the trusty sidekick you didn’t know you needed. This gem lets you harness the magic of AI without the headache of spending weeks in a dark cave of tutorials. With just a sprinkle of modern technology and a dash of simplicity, you can transform those mundane lines of code (you know, the ones that check if a number is even or compare two values) into something truly extraordinary!

## Why conditions-ai? 🤔

- **No More Overwhelm**: Say goodbye to the chaos of figuring out AI on your own. conditions-ai is here to save your sanity!
- **Modern Tech Stack**: Built using the latest and greatest technologies, so you can feel like a coding superhero.
- **Easy AI/GenAI Implementation**: Quickly integrate AI features into your product without the steep learning curve. Seriously, it’s easier than making a cup of coffee!
- **Build using uv**: conditions-ai is built using uv, so you can easily add it to your project with a single command. No fuss, no muss!

So, if you’re ready to level up your SaaS product and impress your boss without pulling your hair out, give **conditions-ai** a whirl! Let’s turn that confusion into confidence and ship some AI-powered features together. 🚀

For all those who want to sprinkle a little AI magic into their product without the sorcery of complicated machine learning—this is for you!


**Inspired by ['is-even-ai'](https://github.com/Calvin-LL/is-even-ai/tree/main) for JS/TS and [this tweet](https://twitter.com/erenbali/status/1766602689863950658).**

## Installation 🛠️

[The package is available on PyPI.](https://pypi.org/project/conditions-ai)

You can install it using `pip`:

```sh
pip install conditions-ai
```

or you can install it using `uv`:

```sh
uv add conditions-ai
```

## Usage 👨‍💻

```python
# Import the ConditionsAI class - currently only OpenAI is supported
from conditions_ai.models.conditions_openai import ConditionsAIOpenAI

if __name__ == "__main__":
    # Set the OS environment variable OPENAI_API_KEY if you don't want to pass the API key as an argument and change the model_id to the model you want to use
    conditions_ai_openai = ConditionsAIOpenAI(openai_api_key="YOUR_OPENAI_API_KEY", openai_model_id="gpt-4o-mini")
    
    print(conditions_ai_openai.is_even(2)) # True
    print(conditions_ai_openai.is_odd(2)) # False
    print(conditions_ai_openai.is_positive(2)) # True
    print(conditions_ai_openai.is_negative(5)) # False
    print(conditions_ai_openai.is_zero(2)) # False
    print(conditions_ai_openai.equal_to(6, 6)) # True
    print(conditions_ai_openai.not_equal_to(6, 6)) # False
    print(conditions_ai_openai.greater_than(6, 5)) # True
    print(conditions_ai_openai.less_than(6, 5)) # False
```

## Supported AI providers 💪

Feel free to make a PR to add more AI platforms.

- [x] [OpenAI](https://openai.com) 
- [ ] [Anthropic](https://www.anthropic.com/)
- [ ] [Groq](https://groq.com/)
- [ ] [Mistral AI](https://mistral.ai/)
- [ ] [Hugging Face](https://huggingface.co/)
- [ ] [Bedrock](https://aws.amazon.com/bedrock)

## Repo Structure 📂

```
.
├── .github
│   └── workflows
│       ├── build_n_release.yml
│       └── tests.yml
├── conditions_ai
│   ├── constants
│   │   ├── __init__.py
│   │   └── prompts.py
│   ├── models
│   │   ├── __init__.py
│   │   └── conditions_openai.py
│   ├── utils
│   │   ├── __init__.py
│   │   └── bool_converter.py
│   └── __init__.py
├── tests
│   ├── __init__.py
│   └── test_openai.py
├── .gitignore
├── .python-version
├── LICENSE
├── pyproject.toml
├── README.md
└── uv.lock
```

## Contributing 🤝

If you want to contribute to this project and make it better, your help is very welcome. Create a pull request with your changes and I will review it. If you have any questions, open an issue.

## License 📝
MIT
