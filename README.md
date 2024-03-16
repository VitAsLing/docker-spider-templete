# Web Scraper

这是一个使用Python和Selenium WebDriver编写的网页爬虫项目。项目的主要功能是打开指定的网页，获取网页的源代码，以及从API获取和发送JSON数据。

## 环境要求

这个项目需要以下环境才能运行：

- Python 3.9 或更高版本
- pip
- Docker
- docker-compose

此外，你还需要安装以下Python库：

- selenium~=4.18.1
- requests~=2.31.0

你可以通过运行以下命令来安装这些库：

```bash
pip install -r requirements.txt
```

## 使用Docker

这个项目包含一个Dockerfile和docker-compose.yml文件，你可以使用Docker来运行这个项目。首先，你需要安装Docker和docker-compose。然后，你可以使用以下命令来构建和运行项目：

```bash
docker-compose up --build
```

## 功能

- `open_webpage_with_chrome(url)`: 打开指定URL的网页，如果失败则重试3次，每次失败后等待3秒
- `get_chrome_options()`: 获取Chrome的选项配置
- `wait_for_page_load(driver)`: 等待网页加载完成
- `check_webpage_status(url)`: 检查网页的状态，如果状态码不是200，则抛出异常
- `get_json_from_api(api_url)`: 从指定的API URL获取JSON数据
- `post_json_to_api(api_url, data)`: 向指定的API URL发送JSON数据

## 测试

这个项目包含了一些单元测试，你可以使用以下命令来运行测试：

```bash
python -m unittest discover test
```

## 贡献

如果你有任何问题或者建议，欢迎提交issue或者pull request。

## 许可证

这个项目使用MIT许可证，详情请见[LICENSE](LICENSE)文件。