+++
title = 'Understanding the Fundamentals and Principles of Modern AI through LLMs, SLMs, MCPs, RAG, GraphDBs, Intelligent Agent Development, and Spec Driven Development'
description = 'An overview of the key concepts behind large language models and their applications.'
tags = ['AI', 'LLM', 'MCP', 'RAG', 'Agents', 'Spec Driven Development']
date = '2026-03-08T16:00:00.000Z'
draft = false
categories = ['AI']
series = []
author = 'Miguel Alvarez'
keywords = ['AI', 'LLM', 'MCP', 'RAG', 'Agents']

[cover]
image = ""
relative = true
+++

It is no news that artificial intelligence is entering our lives, but to fully take advantage of it we must understand how it works. Therefore, in this post, we are going to explore the fundamentals and principles of modern artificial intelligence through LLMs, SLMs, MCPs, RAGs, GraphDBs, and the development of intelligent agents.

## What is an LLM?

A language model is not something magical. Back in 2017 I had already seen the paper on the transformer architecture, the famous "Attention Is All You Need". At that time OpenAI was more of an experiment than anything else, but well, I knew that AI would change every discipline that exists now, as it is happening.

An LLM (Large Language Model) in its foundation is an AI model based on the Transformer architecture. The idea behind this is to build a massive neural network that can predict the next word (or token) in a sequence, given a previous context.

For example, if we give it the sequence "The cat sat on the", the model will predict the next word based on mathematical probabilities, which could be "mat", "chair", "table", etc.

These models are trained with massive amounts of text from the internet, books, and articles, allowing them to learn patterns, grammar, facts, and, surprisingly, an emergent reasoning ability.

{{< figure src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVFR_s-LjFVZjXzdLH8JHSQhSU2vouSp4RBw&s" title="Figure 1: Transformer Architecture." >}}

## Training vs Inference

To understand the AI lifecycle, it is vital to distinguish between these two phases. Training is the construction stage, where the model "reads" terabytes of data and adjusts its trillions of mathematical parameters. It is an extremely expensive process that requires thousands of GPUs (graphics cards) working non-stop for months and consuming millions of dollars in electricity and hardware.

On the other hand, inference is what happens when you ask a finished model a question. In this phase, the AI is no longer learning new information; it is simply applying the mathematical calculations (the weights) it defined during training to generate the predictive response. Inference requires much less computational power, which explains why giant companies train the models, but we can use them (perform inference) from our laptop or phone.

{{< figure src="https://www.profesionalreview.com/wp-content/uploads/2023/11/Entrenamiento-vs-inferencia-IA.jpg" title="Figure 2: Differences between the training phase and the inference phase." >}}

## Attention is all you need

The paper “Attention Is All You Need” (2017) presented the Transformer, the architecture that laid the foundations for modern LLMs. Its attention mechanism allows the model to capture complex and long-range relationships in text sequences without depending on recurrent networks, facilitating large-scale language generation, understanding, and manipulation. Thanks to this, LLMs can learn deep linguistic patterns and extensive contexts, enabling advanced applications such as chatbots, automatic summaries, and intelligent agent systems.

{{< figure src="https://substackcdn.com/image/fetch/$s_!xMer!,w_1200,h_675,c_fill,f_jpg,q_auto:good,fl_progressive:steep,g_auto/https%3A%2F%2Fsubstack-post-media.s3.amazonaws.com%2Fpublic%2Fimages%2Ff4e5c7ab-2fa0-4927-81db-606a2e7bbd07_680x470.png" title="Figure 3: Attention Mechanism in the Transformer." >}}

## Does a model think!?

Thinking is an AI's ability to reason, solve problems, and make decisions. It is the capacity of an AI to reason, solve problems, and make decisions.

This technique is based on generating a "thought diagram" that represents the sequence of ideas and reasoning the AI follows to reach an answer. This is achieved by generating tokens (words) that represent ideas and reasoning, and that the AI can use to generate a response.

Therefore, AI is not capable of thinking, but can only generate responses based on the tokens we provide. As much as it may seem magical.

{{< figure src="https://media.licdn.com/dms/image/v2/D5612AQGTmOjrkfDZlQ/article-cover_image-shrink_720_1280/article-cover_image-shrink_720_1280/0/1730836479297?e=2147483647&v=beta&t=sQmLQHYJibpAW67HzYeKOGSNr5YsIy7BHIUuhXo5KhA" title="Figure 4: The process of reasoning and token generation." >}}

## What is an SLM?

A small language model (SLM) is a language model that has fewer parameters than a traditional LLM. Therefore, it is faster and more efficient, although it may not be as capable in ultra-complex reasoning tasks as a giant LLM.

These are perfect for running on a local machine due to their low resource consumption. A large LLM can easily occupy 70GB of VRAM, which requires a powerful cluster of multiple GPUs. In contrast, an SLM (such as Llama 3 8B or Phi-3) is capable of running on your own GPU or CPU depending on the parameterization.

{{< figure src="https://miro.medium.com/1*xPy7N0q8GoQ4kWflrN4qmQ.png" title="Figure 5: Ecosystem of small language models (SLM)." >}}

## Quantization

Quantization is a technique used to reduce the size of a language model in memory. By default, the weights (the "mathematical instructions") of a model are saved in high-precision format, generally 16-bit (FP16 or BF16), which requires a massive amount of video RAM.

To solve this, we compress the model to 8-bit (INT8) or even 4-bit (INT4) formats. What we do when quantizing is, in essence, "rounding" or truncating the decimal numbers that make up the AI's brain. By reducing this mathematical precision, we slightly increase the model's perplexity (a measure of how "confused" or imprecise it can become in edge cases), but we lose such a minimal fraction of general "intelligence" that for 95% of practical use cases, it is imperceptible.

In return, the benefits are abysmal. This technique democratizes access to AI, allowing the use of several optimized formats according to our hardware.

Thanks to quantization, a model that originally required 30GB of memory can be reduced to 6GB, allowing it to run smoothly and privately on the hardware we have at home.

{{< figure src="https://i0.wp.com/novita-blog.s3.ap-southeast-1.amazonaws.com/simplify-llm-quantization-process-for-success-0%2AO_5tGL0DBIB6argh.png?w=1200&ssl=1" title="Figure 6: Weight quantization process for memory optimization." >}}

## Giving Memory and Context to the AI

No matter how smart an LLM is, its knowledge is frozen at the moment its training ends. If you ask it about your company's sales from yesterday, it will invent an answer (hallucinate). This is where RAG (Retrieval-Augmented Generation) comes in.

RAG is a "dirty" technique based on retrieving relevant text snippets from an external database to give context to the AI; it's dirty because it's not an AI technique, but a hack technique to inject context into the AI through the System Prompt.

Instead of relying exclusively on the model's internal memory, a RAG system takes your question, searches an external database (such as your PDF documents, vector databases, or internal wikis) for the most relevant text snippets, and passes them to the LLM as "context" before it responds. Basically, it's giving the AI a reference text to take an open-book exam.

{{< figure src="https://www.promptingguide.ai/_next/image?url=%2F_next%2Fstatic%2Fmedia%2Frag-framework.81dc2cdc.png&w=3840&q=75" title="Figure 7: Retrieval-Augmented Generation (RAG) Flow." >}}

## Understanding Complex Relationships

Vector databases are the standard for RAG, but sometimes they lack deep relational context. Graph-oriented databases (GraphDBs), such as Neo4j, store information in the form of nodes (entities) and edges (relationships).

When we combine GraphDBs with LLMs (a technique known as GraphRAG), the AI not only finds statistically similar text snippets but understands the topology of the information: "Company A is a supplier of Company B, whose CEO was an investor in project C". This allows the AI to perform reasoning on complex information networks that a traditional RAG would miss.

{{< figure src="https://www.luisllamas.es/images/20297/grafo-dirigido.webp" title="Figure 8: Structure of a directed graph in relational databases." >}}

## Anthropic's Model Context Protocol

The Model Context Protocol (MCP) is a recent and revolutionary open standard from Anthropic. Imagine that every time you wanted to connect your LLM to your Google Drive, your SQL database, or a local weather API, you had to write and maintain a custom integration code.

MCP works like a "universal plug", standardizing how AI assistants request information and how local or remote tools deliver it securely. This greatly facilitates the creation of ecosystems where AI interacts with your real work environment without friction.

{{< figure src="https://miro.medium.com/0*ydhvFVVoKyOfEHMi.png" title="Figure 9: Model Context Protocol facilitating tool integration." >}}

## Intelligent Agents

Imagine it's Friday at 5:00 PM and you receive a last-minute email: "I need a detailed analysis of the competition against our current prices for Monday first thing." In the world of standard LLMs, you prepare for a weekend of copying, pasting, and searching for data because although AI is brilliant at writing, it remains a passive entity that just spits out text and waits for your next command.

But this is where Intelligent Agents come in to change the game. Instead of being a simple oracle, an agent uses the LLM as its "reasoning engine" to execute complete tasks. When you ask for that analysis, the agent decides that its first step should be to activate a web search tool through MCP to locate your competitors and extract fresh data from their official sites.

While you get up for a coffee, the agent detects that the web data is not enough for a real comparison, so it autonomously consults your internal database via RAG to contrast those findings with your current inventory. If along the way it runs into a connection error or a blocked website, it doesn't give up or send you an error message; it enters a feedback loop, corrects its own strategy, and searches for an alternative source. At the end of the process, the agent writes the report, structures the conclusions, and saves the document directly on your computer. When you return to your desk, the work of an entire weekend is ready. It is the definitive jump from an AI that answers questions to a proactive partner that solves problems.

{{< figure src="https://www.tirsomaldonado.es/wp-content/uploads/2025/04/agentesinteligentes.jpg" title="Figure 10: Operational cycle of an autonomous intelligent agent." >}}

## The problem of OpenClaw and the agents

Not everything is a bed of roses in the deployment of agents with OpenClaw. Although the promise of an AI that "navigates for you" is fascinating, the first big wall is latency and token consumption. Every time an OpenClaw agent takes a screenshot of your screen to decide where to click, it is sending a massive amount of visual data to the model. This not only skyrockets the API bill but creates a delay that makes it, sometimes, faster to do the task yourself than to wait for the agent to process the next step.

The second critical problem is the fragility of reasoning. OpenClaw depends on the LLM perfectly understanding the user interface. If a website updates a button or an unexpected pop-up appears, the agent can enter a "hallucination loop", trying to click on elements that no longer exist or getting lost in infinite tasks. Additionally, there is the giant elephant in the room: security. Giving an OpenClaw-based agent full access to your browser and your credentials (via MCP) is opening a backdoor. If the model is manipulated through a prompt injection from a malicious website that the agent is visiting, you could end up with an agent emptying your own database without you realizing it.

{{< figure src="https://www.malwarebytes.com/wp-content/uploads/sites/2/2026/02/OpenClaw_logo.png" title="Figure 11: OpenClaw logo and the challenge of security in agents." >}}

## Spec Driven Development

The term Spec Driven Development (SDD) is born from the need to move from "prompts" towards engineering rigor. In traditional development, we write code; in AI-assisted development, we often make the mistake of simply "chatting" with the model expecting it to guess our intention. SDD breaks this by establishing that the specification is the only source of truth.

Instead of throwing a vague instruction at an agent, the flow begins by defining a rigorous technical contract (usually in Markdown or JSON). This specification details not only the final goal but also the business rules, the data schemas to be respected, and the interfaces of the tools it will consume through MCP.

The fascinating thing about SDD is that it transforms the programmer's role: you stop being the one writing code to become the architect who defines the constraints. The agent uses this spec as a "safety rail". Before executing any action, the model validates its plan against the specification; if the result of a search or code generation does not meet the defined technical requirements, the system enters a self-correction loop until it aligns with the initial contract.

This solves the big problem of LLM unpredictability. By combining Spec Driven Development with autonomous agents, we go from an AI that "hallucinates solutions" to an AI that "implements requirements". It is, in essence, applying the scientific method and software architecture to the wild west of generative artificial intelligence.

{{< figure src="https://media.licdn.com/dms/image/v2/D5612AQEjgppxW_thsw/article-cover_image-shrink_720_1280/B56Zl.tJnjHQAI-/0/1758767389899?e=2147483647&v=beta&t=V4gQnyVUtovTmwd7-KvKeNn9wjWwk-mxI8T4a70rwPw" title="Figure 12: Spec Driven Development as a rigorous framework." >}}

## Code is still important

I don't like to hear that code no longer matters. Those who claim this are deeply mistaken: engineering, like mathematics, is by nature deterministic. Nor do I consider AI to be a simple "abstraction jump" per se (although it shares certain similarities). Historically in computing, every time we moved up an abstraction level, we still had clear and precise instructions that the program had to execute. Today, however, a prompt does not always guarantee the same result. It is precisely from this need for control that Spec-Driven Development is born.

{{< figure src="https://tvd12.com/api/v1/media/ba2b79849fa1720ed9331c507474ee101a42fde5df548bdf738258247406b902.jpg" title="Figure 13: Torvalds, Show me the code." >}}

## The future

The future of artificial intelligence does not involve only creating increasingly immense and expensive monolithic models, but weaving ecosystems of specialized and efficient components. The trend points to a world where we will orchestrate multi-agent systems using small local models (quantized SLMs) for fast, low-cost tasks, reserving the raw power of massive cloud LLMs only for deep reasoning.

AI will cease to be a simple "text box" we consult, to transform into an invisible computational layer, interacting with our environments through open standards like MCP and orchestrated under the rigid rules of Spec Driven Development. In this new horizon, predictive software will not replace deterministic software but will integrate into it. That is why the figure of the engineer, version control, and structured code will be more important than ever to give order, security, and meaning to the infinite generative possibilities.

{{< figure src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQmOIg6sdauB162o5ccCmX_6vCb1kkNiViLTw&s" title="Figure 14: Future vision of integrated and orchestrated AI." >}}
