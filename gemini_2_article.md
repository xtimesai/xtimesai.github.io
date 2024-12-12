# Introduction

Hi, welcome to another video. This video is about the new Gemini 2.0 Flash model.

## About Gemini 2.0 Flash

Gemini 2.0 Flash was launched just yesterday, and the model is performing amazingly. It has so much capability, outperforming Gemini 1.5 Pro 2. It supports real-time multimodal features, like analyzing videos, and can natively generate audio and images. This is pretty mind-blowing. If you've seen my last video, you'll know it performs extremely well, much better than Claude 3.5 Haiku and on par with Sonet. It's also free to use via Google AI Studio, and the API is also free with very generous rate limits. Technically, even if you wanted to pay, you can't because pricing is not yet sorted out, and it is still experimental. So, you can only use it for free, which is pretty cool.

I've talked about other aspects in my previous video, so check that out for more details. But today's video is about how you can use the Gemini 2.0 model with Aider and Klein for AI coding, completely free, and get amazing results similar to Sonet, also for free.

First, let's discuss the exact limits on Gemini 2.0 Flash. You get 10 requests per minute, along with 4 million max tokens per minute, and 1500 requests per day, all for free. This is great, and I don't think you'll ever exceed this limit. Another thing to mention is that Gemini has about a 2 million context window, which is also great.

## AI Coding Setups

Let's start with the AI coding setups. I'll begin with Aider. Aider has recently updated their leaderboards with the new model, and it performs pretty well, although it still doesn't quite match Sonet.

### Setup with Cline & Aider

First, go to Google AI Studio. You'll see the models there. I've explained in my previous video how to use it. You'll see the Gemini 2 experimental model, where you can send basic messages. If you use the model via Google AI Studio, there's no rate limit, and you can use it unlimited times for free. However, the API does have a rate limit, as I mentioned earlier.

Click the "Get API key" option and create an API key. Keep it in a safe place, as we'll need it later. Once you have that, open the terminal. First, make sure you update Aider, or install it if you're new. You can do that with the command `aider --update`. Next, you'll need to export the Gemini API key that you got from Google AI Studio, like this: `export GEMINI_API_KEY=your_api_key`. You'll need to do this every time you open the terminal, but you can also create an environment file and put the API keys there, so it starts with those keys every time.

Once that's done, we can start Aider with the model flag and Gemini flash 2.0 experimental, like this: `aider --model gemini-2.0-flash-experimental`. If you don't want to type the big model name every time, add another `aider_model` variable to your environment file and put the Gemini 2.0 flash model there. Then, you can just run `aider`, and it will automatically pick up the default Gemini 2.0 flash model.

I have a basic Expo app here. I'm going to ask it to make a water tracker app, as it's a common prompt. Let's see how well it performs. One great thing about Gemini Flash is that it's super fast. You don't get the slow response you get with Claude or others. It's super fast. Here's the code, and you can approve it. The generation looks pretty good. This is just a demo, but I've tried it with more complex things, and it's better than 3.5 Haiku in most general use cases. It's much more reliable than the previous Pro and Flash models. This is great, especially since it's free.

### Using Gemini with Klein

Now, let me show you how you can use it in Klein as well. Klein hasn't updated the Gemini model section to account for the new flash model, which is a bummer. But once it's available, you should be able to select the model there. For now, you can use it via the OpenAI compatible option. Gemini now has an OpenAI compatible API. Enter the base URL, the API key, and the Gemini flash model name. Once set up, Klein should start working.

I'm not doing any thorough testing here, so I'll just ask it to make a simple Finance Tracker app using HTML, CSS, and JS. One thing I've noticed is that the function calling capabilities of this model are extremely great. Previous Gemini models were a hit and miss, but this one is amazing. It makes sense that they are promoting this model as an agentic model. It also supports a long context window, which is a lifesaver for coding. I think Klein and Aider can also take advantage of the new real-time audio and image generation.

It's now done, so let's run it and see. This worked pretty well, and that's how you can use it with Klein as well. I've switched to this model now because it's like 70% of Sonet for free, which is great for me. I can always switch between models when I feel like it. This is a great model for sure.

Let me know if you guys want a video where I create a full-stack app with it.

## Ending

Overall, it's pretty cool. Let me know your thoughts in the comments. If you liked this video, consider donating to my channel through the super thanks option below, or you can also consider becoming a member by clicking the join button. Also, give this video a thumbs up and subscribe to my channel. I'll see you in the next video. Till then, bye.

---

# 介绍

你好，欢迎观看另一个视频。该视频是关于新的 Gemini 2.0 Flash 模型的。

## 关于 Gemini 2.0 Flash

Gemini 2.0 Flash昨天刚刚推出，该型号的表现令人惊叹。它的功能非常强大，优于 Gemini 1.5 Pro 2。它支持实时多模式功能，例如分析视频，并且可以本地生成音频和图像。这真是令人兴奋。如果您看过我的上一个视频，您就会知道它的性能非常好，比 Claude 3.5 Haiku 好得多，与 Sonet 不相上下。它也可以通过 Google AI Studio 免费使用，并且 API 也是免费的，但有非常慷慨的速率限制。从技术上讲，即使你想付费，你也不能付费，因为定价尚未确定，而且仍处于实验阶段。所以，你只能免费使用它，这很酷。

我在之前的视频中讨论了其他方面，因此请查看以了解更多详细信息。但今天的视频是关于如何使用 Gemini 2.0 模型与 Aider 和 Klein 进行 AI 编码，完全免费，并获得类似于 Sonet 的惊人结果，也是免费的。

首先，我们来讨论一下 Gemini 2.0 Flash 的具体限制。您每分钟获得 10 个请求，每分钟最多获得 400 万个令牌，每天获得 1500 个请求，全部免费。这太棒了，我认为您永远不会超过这个限制。另外值得一提的是，Gemini 有大约 200 万个上下文窗口，这也很棒。

## AI 编码设置

让我们从人工智能编码设置开始。我将从艾德开始。 Aider 最近用新模型更新了他们的排行榜，它的表现相当不错，尽管它仍然与 Sonet 不太匹配。

### 与 Cline 和 Aider 一起设置

首先，进入Google AI Studio。您会在那里看到模型。我在之前的视频中已经解释过如何使用它。您将看到 Gemini 2 实验模型，您可以在其中发送基本消息。如果您通过 Google AI Studio 使用该模型，则没有速率限制，并且可以无限次免费使用。然而，正如我之前提到的，API 确实有速率限制。

单击“获取 API 密钥”选项并创建 API 密钥。将其保存在安全的地方，因为我们稍后会需要它。完成后，打开终端。首先，请确保您更新了 Aider，如果您是新用户，请安装它。您可以使用命令“aider --update”来完成此操作。接下来，您需要导出从 Google AI Studio 获得的 Gemini API 密钥，如下所示：“export GEMINI_API_KEY=your_api_key”。每次打开终端时都需要执行此操作，但您也可以创建一个环境文件并将 API 密钥放在那里，这样每次都会以这些密钥开始。

完成后，我们可以使用模型标志和 Gemini flash 2.0 实验启动 Aider，如下所示：“aider --model gemini-2.0-flash-experimental”。如果您不想每次都输入大模型名称，请在环境文件中添加另一个“aider_model”变量，并将 Gemini 2.0 flash 模型放在那里。然后，你可以运行`aider`，它会自动选择默认的Gemini 2.0闪存模型。

我这里有一个基本的 Expo 应用程序。我将要求它制作一个水追踪应用程序，因为这是一个常见的提示。让我们看看它的表现如何。 Gemini Flash 的一大优点是速度超快。你不会像克劳德或其他人那样得到缓慢的反应。速度超级快。这是代码，您可以批准它。这一代看起来还不错。这只是一个演示，但我已经尝试过更复杂的东西，并且在大多数一般用例中它比 3.5 Haiku 更好。它比以前的 Pro 和 Flash 型号可靠得多。这很棒，特别是因为它是免费的。

### 与 Klein 一起使用 Gemini

现在，让我向您展示如何在 Klein 中使用它。 Klein 还没有更新 Gemini 模型部分来解释新的 flash 模型，这真是令人遗憾。但一旦可用，您应该能够在那里选择型号。目前，您可以通过 OpenAI 兼容选项使用它。 Gemini 现在拥有兼容 OpenAI 的 API。输入基本 URL、API 密钥和 Gemini 闪存型号名称。设置完毕后，克莱因就应该开始工作了。

我在这里没有进行任何彻底的测试，所以我只是要求它使用 HTML、CSS 和 JS 制作一个简单的 Finance Tracker 应用程序。我注意到的一件事是该模型的函数调用能力非常出色。以前的 Gemini 型号很受欢迎，但这款却令人惊叹。他们将这种模型作为代理模型来推广是有道理的。它还支持长上下文窗口，这对于编码来说是一个救星。我认为 Klein 和 Aider 也可以利用新的实时音频和图像生成功能。

现在已经完成了，让我们运行一下看看。这非常有效，您也可以将它与 Klein 一起使用。我现在已经切换到这个模型，因为它就像免费的 Sonet 的 70%，这对我来说很棒。当我愿意时，我随时可以在模型之间切换。这无疑是一个很棒的模型。

如果你们想要一个视频，让我知道我用它创建了一个全栈应用程序。

## 结束

总的来说，它非常酷。在评论中让我知道您的想法。如果您喜欢这个视频，请考虑通过下面的超级感谢选项向我的频道捐款，或者您也可以考虑通过单击加入按钮成为会员。另外，请给这个视频点赞并订阅我的频道。我们将在下一个视频中见到您。到那时，再见。
