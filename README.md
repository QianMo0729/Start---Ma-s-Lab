# Ma's Lab 入门学习记录

本仓库整理课题组入门阶段的学习要求、理论阅读材料、课程证书、第一周报告及数据分析代码。学习计划覆盖 Visualization、HCI 与大模型 Agent 三个方向，具体任务和报告要求见入门清单。

## 阅读入口

- [课题组入门学习材料清单](课题组入门学习材料清单.md)
- [第一周学习报告（PDF）](Report/Phase1/Week1_Report.pdf)
- [报告 LaTeX 源文件](Report/Phase1/Week1_Report.tex)
- [薪资数据分析脚本](Report/Phase1/Analyze/database_analyze.py)

## 目录

```text
.
├── README.md
├── 课题组入门学习材料清单.md
├── 理论材料/
│   ├── Evaluating User Interface Systems Research.pdf
│   └── LLM_Powered_Autonomous_Agents.pdf
├── Cartificates/
│   ├── QianMoA - Python.png
│   ├── QianMoA - Pandas.png
│   └── ResponseWebDesing.png
├── Dataset/
│   ├── salaries.csv
│   └── salaries.json
└── Report/Phase1/
    ├── Week1_Report.pdf
    ├── Week1_Report.tex
    └── Analyze/database_analyze.py
```

## 课程证书

以下日期按仓库内证书图片标注记录。

| 课程 | 证书日期 | 文件 |
| --- | --- | --- |
| Kaggle Python | 2026-10-02 | [Python 证书](Cartificates/QianMoA%20-%20Python.png) |
| Kaggle Pandas | 2026-10-03 | [Pandas 证书](Cartificates/QianMoA%20-%20Pandas.png) |
| freeCodeCamp 响应式网页设计 | 2026-10-03 | [响应式网页设计证书](Cartificates/ResponseWebDesing.png) |

## 数据与分析

报告注明的数据来源为 Kaggle 的 [Data Science, AI & ML Job Salaries in 2025](https://www.kaggle.com/datasets/adilshamim8/salaries-for-data-science-jobs)。仓库保存了 `salaries.csv` 和 `salaries.json`，当前分析脚本使用 CSV 文件。

脚本检查数据规模、缺失值和重复记录，整理文本字段，并排除美元薪资缺失或不大于零的记录，再输出薪资描述统计、岗位数量、经验等级分组统计和公司所在地占比。脚本会统计完全重复的记录，但不会删除这些记录；结果输出到终端，不另存清洗后的文件。

运行需要 Python 3 和 pandas。先在仓库根目录创建环境并安装依赖：

```bash
python3 -m venv .venv
source .venv/bin/activate
python -m pip install pandas
```

脚本中的 `url` 当前是作者电脑上的绝对路径。其他环境运行前，先将该行改为：

```python
url = "Dataset/salaries.csv"
```

然后保持工作目录为仓库根目录，执行：

```bash
python Report/Phase1/Analyze/database_analyze.py
```

## 报告源文件

可以直接阅读仓库内的报告 PDF。若需重新编译 `.tex`，使用支持中文的 XeLaTeX 环境；源文件中的三张证书图片目前同样使用本机绝对路径，需要先按自己的目录修改图片路径。
