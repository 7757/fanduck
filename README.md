<p align="center"><strong>💬 Microduck 资源分享交流群</strong></p>

<p align="center"><strong>简体中文</strong> · <a href="README.en.md">English</a></p>

<p align="center">
  <a href="assets/wechat-group-qr.png">
    <img src="assets/wechat-group-qr.png" alt="微信扫码加入 Microduck 资源分享交流群，二维码于 9 月 23 日前有效" width="400" />
  </a>
</p>

<p align="center">微信扫码入群，一起交流复刻与制作。点击二维码可查看原图。<br />当前二维码：<strong>2026 年 9 月 23 日前有效</strong>。</p>

---

# 超能花钱鸭 Fanduck · Microduck 已复刻成功

> **基于官方项目完成复刻**：本项目基于 Pollen Robotics 官方公开的 [Microduck 代码](https://github.com/pollen-robotics/microduck) 与 [模型资料](https://github.com/pollen-robotics/microduck_rl) 制作。感谢官方团队的分享！

**[官方项目](https://github.com/pollen-robotics/microduck) · [官方官网](https://pollen-robotics.com/microduck/) · [我们的官网](https://duck.fandcode.com/)**

**我们的 Microduck 已经复刻成功！** 从零件采购、3D 打印到装配与调试，我们完成了从 0 到 1 的实机复刻，下面的照片和视频就是这只鸭子的实拍。

Fanduck 是对 Pollen Robotics Microduck 的非官方个人研究复刻。这里分享本次复刻所用的制作资料：物料清单、打印文件、板件资料、制作工具，以及查看鸭子 3D 姿态的镜像工作台。资料与项目官网同步存放，方便大家参考和交流。

## 我们的鸭子

<p align="center">
  <img src="assets/fanduck.webp" alt="超能花钱鸭实拍：侧面结构与打印外壳" height="360" />
  <img src="assets/fanduck-back.webp" alt="超能花钱鸭实拍：背部电池与双腿装配" height="360" />
</p>

## 实机演示

**实拍一**

<p align="center">
  <img src="assets/fanduck-demo.gif" alt="超能花钱鸭实拍动态演示：约 12 秒循环 GIF" width="360" />
</p>

**实拍二**

<p align="center">
  <img src="assets/fanduck-demo-02.gif" alt="超能花钱鸭第二段实机演示：约 19 秒循环 GIF" width="320" />
</p>

## 制作资料下载

当前资料版本：`maker-20260916`。以下 4 个 ZIP 与官网发布目录中的文件完全一致。

| 资料包 | 包含什么 | 下载 |
| --- | --- | --- |
| 制作物料与打印文件 | 物料清单、中文分类打印件、装配图 | [ZIP · 12.7 MB](downloads/maker-20260916/fanduck-materials-print-20260916.zip?raw=true) |
| 板件制造资料 | Robot HAT、电池触点板、NFC 图纸及制造文件 | [ZIP · 31.3 MB](downloads/maker-20260916/fanduck-boards-20260916.zip?raw=true) |
| 制作工具源码 | 打印修正版生成、几何检查脚本及必要输入 | [ZIP · 1.1 MB](downloads/maker-20260916/fanduck-making-tools-20260916.zip?raw=true) |
| 3D 镜像工作台源码 | 3D 姿态显示、只读关节采集、可选视频观察 | [ZIP · 2.6 MB](downloads/maker-20260916/fanduck-mirror-workbench-20260916.zip?raw=true) |

第一次看这个项目，可以先下载“制作物料与打印文件”，从包内的 `01_物料清单.md` 开始。其余包按需要下载，使用前阅读各自的 README。

下载清单见 [manifest.json](downloads/maker-20260916/manifest.json)，完整性校验见 [SHA256SUMS.txt](downloads/maker-20260916/SHA256SUMS.txt)。在 macOS 或安装了 `shasum` 的终端中，从仓库根目录运行：

```bash
cd downloads/maker-20260916
shasum -a 256 -c SHA256SUMS.txt
```

## 来源与许可

感谢 [Pollen Robotics](https://github.com/pollen-robotics/microduck) 公开的 Microduck 资料。上游来源、版本、许可与署名保留在各个包内，见 `SOURCES.json`、`LICENSES/` 及 README。

机械模型及衍生件保留上游的 **CC BY-SA-NC 非商业许可**，软件许可不能覆盖模型的商业使用；本项目不代表完整开源硬件。具体范围见[许可与来源说明](LICENSES.md)，打印、板件和设备连接的使用限制请以包内说明为准。

欢迎 Star 收藏资料，也欢迎分享你的制作进展。项目更新、照片与视频继续发布在 **[超能花钱鸭官网](https://duck.fandcode.com/)**。
