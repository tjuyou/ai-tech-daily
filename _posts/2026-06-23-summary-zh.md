---
layout: default
title: "Horizon Summary: 2026-06-23 (ZH)"
date: 2026-06-23
lang: zh
---

> 从 7 条内容中筛选出 5 条重要资讯。

---

1. [Valve 推出 Steam Machine，采用公平预订系统](#item-1) ⭐️ 9.0/10
2. [Moebius：0.2B 参数修补模型达到 10B 级性能](#item-2) ⭐️ 8.0/10
3. [警察局长滥用 Flock 车牌读取器数据跟踪女性](#item-3) ⭐️ 8.0/10
4. [加拿大计划到 2040 年建造 10 座核反应堆](#item-4) ⭐️ 7.0/10
5. [英伟达 5.4 万亿美元市值：AI 模型公司沦为算力佃农](#item-5) ⭐️ 5.0/10

---

<a id="item-1"></a>
## [Valve 推出 Steam Machine，采用公平预订系统](https://store.steampowered.com/news/group/45479024/view/685257114654870245) ⭐️ 9.0/10

Valve 于 2026 年 6 月 22 日推出了 Steam Machine，这是一款运行 SteamOS 的游戏 PC，采用随机预订系统以防止黄牛并确保公平。 此次发布标志着 Valve 以开放平台重返专用游戏硬件领域，通过提供客厅友好的外形和 PC 游戏的灵活性，可能颠覆主机市场。 Steam Machine 起售价为 1049 美元，采用 6 月 22 日至 25 日开放的随机预订队列，并强调开放性——用户可以安装其他操作系统或应用程序。

hackernews · theschwa · 6月22日 17:09 · [社区讨论](https://news.ycombinator.com/item?id=48632884)

**背景**: Steam Machine 是 Valve 设计的游戏 PC，运行基于 Linux 的 SteamOS，并通过 Proton 兼容层运行 Windows 游戏。它延续了 2015 年未能成功的早期 Steam Machine 计划。新款旨在结合主机的简便性和 PC 的开放性。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://www.theverge.com/games/952191/valve-steam-machine-reservation-preorder-process">Here’s how you can reserve a Steam Machine | The Verge</a></li>
<li><a href="https://www.pcgamer.com/hardware/gaming-pcs/steam-machine-reservations/">Sign up for a Steam Machine before June 25: Valve running one-time randomized queue due to limited availability and to 'limit resellers' | PC Gamer</a></li>
<li><a href="https://www.tomshardware.com/video-games/console-gaming/valve-opens-steam-machine-reservations-details-usd1-049-starting-price-randomized-queue-to-stop-scalpers-and-limited-inventory">Valve opens Steam Machine reservations — details $1,049 starting price, randomized queue to stop scalpers, and limited inventory | Tom's Hardware</a></li>

</ul>
</details>

**社区讨论**: 社区评论赞扬了公平的预订系统和开放平台，用户赞赏 Valve 反对锁定的立场。一些人表达了购买兴趣，而另一些人则讨论定价和规格。

**标签**: `#gaming`, `#hardware`, `#valve`, `#steam`, `#pc`

---

<a id="item-2"></a>
## [Moebius：0.2B 参数修补模型达到 10B 级性能](https://hustvl.github.io/Moebius/) ⭐️ 8.0/10

研究人员发布了 Moebius，一个 0.2B 参数的图像修补模型，声称其性能可与 10B 参数模型相媲美。该模型专为高效部署设计，并已在基于浏览器的演示中得到展示。 这一突破可能显著降低高质量图像修补的计算成本和硬件要求，使其更广泛地适用于各类用户和应用场景。它挑战了“更大模型必然带来更优性能”的固有观念。 Moebius 的输出分辨率限制为 512x512，这可能会限制其在高分辨率图像中的实际应用。社区测试指出，修复区域可能明显比周围区域更平滑，且模型在处理新颖物体时表现不佳。

hackernews · DSemba · 6月22日 13:53 · [社区讨论](https://news.ycombinator.com/item?id=48630171)

**背景**: 图像修补是指用合理的内容填充图像中缺失或损坏区域的任务。拥有数十亿参数的大模型取得了令人印象深刻的结果，但需要大量的计算资源。Moebius 旨在以极少的参数实现相近的质量，从而弥合这一差距。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://huggingface.co/papers/2606.19195">Paper page - Moebius: 0.2B Lightweight Image Inpainting ...</a></li>
<li><a href="https://arxiv.org/abs/2606.19195">[2606.19195] Moebius: 0.2B Lightweight Image Inpainting ...</a></li>
<li><a href="https://arxiv.org/html/2606.19195v1">Moebius: 0.2B Lightweight Image Inpainting Framework with 10B ...</a></li>

</ul>
</details>

**社区讨论**: 社区反应不一：一些用户对其效率印象深刻，并创建了浏览器演示，而另一些用户则质疑其声称的 10B 级性能，指出可见的质量差距和分辨率限制。有用户不熟悉“inpainting”一词并请求解释，表明该术语可能并不广为人知。

**标签**: `#image inpainting`, `#efficient AI`, `#computer vision`, `#deep learning`

---

<a id="item-3"></a>
## [警察局长滥用 Flock 车牌读取器数据跟踪女性](https://ipvm.com/reports/police-chiefs-track) ⭐️ 8.0/10

一份报告揭露，警察局长滥用 Flock 的自动车牌读取器（ALPR）数据来跟踪女性，凸显了在访问此类监控数据前需要获得搜查令的紧迫性。 这一事件凸显了 Flock 等大规模监控技术的系统性风险，即使是高级官员也可能为个人利益滥用访问权限，侵蚀公众信任和隐私。这加强了需要法律保障（如搜查令要求）以防止滥用的论据。 Flock 的 ALPR 摄像头捕捉车辆细节并提供可搜索数据，执法部门可以访问这些数据。报告指出，尽管 Flock 和警方列举了破案好处，但最常见的滥用形式是官员跟踪他们认识的人，正如本案所示。

hackernews · jhonovich · 6月22日 19:13 · [社区讨论](https://news.ycombinator.com/item?id=48634694)

**背景**: Flock Safety 是一家运营自动车牌识别摄像头网络的公司，常被警方用于监控。这些摄像头拍摄所有过往车辆并将数据存储在云端，支持搜索和警报。批评者认为，此类大规模监控系统缺乏足够的监督，容易被滥用，正如这份报告所展示的。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/Flock_Safety">Flock Safety - Wikipedia</a></li>
<li><a href="https://www.aclu.org/news/privacy-technology/flock-roundup">Flock’s Aggressive Expansions Go Far Beyond Simple Driver Surveillance | American Civil Liberties Union</a></li>

</ul>
</details>

**社区讨论**: 评论者对声称滥用罕见但最常见形式是跟踪熟人的矛盾表示担忧。有人指出，没有监控，滥用是不可避免的。其他人则将其与虚构的监控场景相类比，突显了现实世界中滥用的可能性。

**标签**: `#privacy`, `#surveillance`, `#police accountability`, `#technology ethics`

---

<a id="item-4"></a>
## [加拿大计划到 2040 年建造 10 座核反应堆](https://www.cbc.ca/news/politics/federal-nuclear-strategy-9.7244509) ⭐️ 7.0/10

加拿大联邦政府宣布了一项核能战略，计划到 2040 年建造多达 10 座新核反应堆，其中至少一座位于安大略省以外。 这标志着重大政策转变，可能重塑加拿大的能源结构，利用其铀储量和 CANDU 技术专长来满足日益增长的基础负荷需求并支持净零目标。 建设成本可能超过 1000 亿美元，政府尚未明确融资方式。该战略还旨在通过燃料、专有技术和出口扩大加拿大在全球核能领域的领导地位。

hackernews · geox · 6月22日 19:06 · [社区讨论](https://news.ycombinator.com/item?id=48634585)

**背景**: CANDU（加拿大氘铀）是一种加拿大加压重水反应堆设计，使用天然铀燃料和重水作为慢化剂。加拿大拥有世界上最大的铀储量之一，并在达林顿等地拥有建造和翻新 CANDU 反应堆的丰富经验。

<details><summary>参考链接</summary>
<ul>
<li><a href="https://en.wikipedia.org/wiki/CANDU_reactor">CANDU reactor - Wikipedia</a></li>
<li><a href="https://natural-resources.canada.ca/energy-sources/nuclear-energy-uranium/nuclear-energy-strategy-canada">Nuclear Energy Strategy for Canada - Natural Resources Canada</a></li>
<li><a href="https://www.cbc.ca/news/politics/federal-nuclear-strategy-9.7244509">Energy minister plans 'nuclear renaissance' with up to 10 ...</a></li>

</ul>
</details>

**社区讨论**: 评论者普遍支持该计划，提及加拿大的铀储量和 CANDU 技术专长，但一些人对时间表表示怀疑，指出英国欣克利角等核项目的历史延误。其他人则强调了达林顿小型模块化反应堆的持续工作。

**标签**: `#nuclear energy`, `#Canada`, `#energy policy`, `#CANDU`, `#infrastructure`

---

<a id="item-5"></a>
## [英伟达 5.4 万亿美元市值：AI 模型公司沦为算力佃农](https://mp.weixin.qq.com/s?__biz=MzI3MTA0MTk1MA==&mid=2652708232&idx=3&sn=a63e5cf64de5f257f8586bb21fa96db0) ⭐️ 5.0/10

一篇文章声称英伟达以 5.4 万亿美元市值成为 AI 硬件最大供应商，将 AI 公司描绘成依赖英伟达 GPU 的佃农。 这凸显了英伟达对 AI 计算资源的绝对控制，引发对市场垄断和 AI 初创公司脆弱性的担忧。 文章语气耸人听闻，缺乏具体技术细节或数据支持其主张，未提供具体例子或数字。

rss · 新智元(微信公众号) · 6月21日 07:00

**背景**: 英伟达的 GPU 是训练大型 AI 模型的关键，使该公司拥有巨大影响力。许多 AI 初创公司依赖使用英伟达硬件的云服务商，从而形成依赖关系。

**标签**: `#AI`, `#Nvidia`, `#hardware`, `#industry-analysis`

---