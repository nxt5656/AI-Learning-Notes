# 配置文件用于实验室
c = get_config()  # noqa

#------------------------------------------------------------------------------#
# 应用程序（SingletonConfigurable）配置
#------------------------------------------------------------------------------#

## 这是一个应用程序。

# 日志格式中用于 %(asctime)s 的日期格式
# 默认值: '%Y-%m-%d %H:%M:%S'
# c.Application.log_datefmt = '%Y-%m-%d %H:%M:%S'

# 日志格式模板
# 默认值: '[%(name)s]%(highlevel)s %(message)s'
# c.Application.log_format = '[%(name)s]%(highlevel)s %(message)s'

# 设置日志级别，可以是值或名称。
# 选项: [0, 10, 20, 30, 40, 50, 'DEBUG', 'INFO', 'WARN', 'ERROR', 'CRITICAL']
# 默认值: 30
# c.Application.log_level = 30

# 配置额外的日志处理器。
# 默认的标准错误日志处理器由 log_level、log_datefmt 和 log_format 设置配置。
# 可以使用此配置将日志输出到文件或对默认处理器进行更精细的控制。
# 如果提供，应为一个日志配置字典，更多信息请参见：
# https://docs.python.org/3/library/logging.config.html#logging-config-dictschema
# 示例：添加一个新处理器，将日志写入文件。
#
# c.Application.logging_config = {
#     "handlers": {
#         "file": {
#             "class": "logging.FileHandler",
#             "level": "DEBUG",
#             "filename": "<path/to/file>",
#         }
#     },
#     "loggers": {
#         "<application-name>": {
#             "level": "DEBUG",
#             # 注意：如果默认的 "console" 处理器没有列出，这里将被禁用
#             "handlers": ["console", "file"],
#         },
#     },
# }
# 默认值: {}
# c.Application.logging_config = {}

# 不启动应用程序，而是将配置输出到标准输出
# 默认值: False
# c.Application.show_config = False

# 不启动应用程序，而是将配置以 JSON 格式输出到标准输出
# 默认值: False
# c.Application.show_config_json = False

#------------------------------------------------------------------------------#
# JupyterApp（Application）配置
#------------------------------------------------------------------------------#

## Jupyter 应用程序的基类

# 对任何提示回答“是”。
# 默认值: False
# c.JupyterApp.answer_yes = False

# 配置文件的完整路径。
# 默认值: ''
# c.JupyterApp.config_file = ''

# 指定加载的配置文件。
# 默认值: ''
# c.JupyterApp.config_file_name = ''

# 生成默认配置文件。
# 默认值: False
# c.JupyterApp.generate_config = False

# 日志格式中用于 %(asctime)s 的日期格式
# 参见 Application.log_datefmt
# c.JupyterApp.log_datefmt = '%Y-%m-%d %H:%M:%S'

# 日志格式模板
# 参见 Application.log_format
# c.JupyterApp.log_format = '[%(name)s]%(highlevel)s %(message)s'

# 设置日志级别，可以是值或名称。
# 参见 Application.log_level
# c.JupyterApp.log_level = 30

# 日志配置
# 参见 Application.logging_config
# c.JupyterApp.logging_config = {}

# 不启动应用程序，而是将配置输出到标准输出
# 参见 Application.show_config
# c.JupyterApp.show_config = False

# 不启动应用程序，而是将配置以 JSON 格式输出到标准输出
# 参见 Application.show_config_json
# c.JupyterApp.show_config_json = False

#------------------------------------------------------------------------------#
# ExtensionApp（JupyterApp）配置
#------------------------------------------------------------------------------#

## 可配置 Jupyter 服务器扩展应用程序的基类。
# ExtensionApp 子类可以通过两种方式初始化：
# - 扩展被列为 jpserver_extension，ServerApp 调用其 load_jupyter_server_extension 类方法。
# - 直接通过调用其 `launch_instance` 类方法启动扩展。此方法可以在扩展的 setup.py 中设置为入口点。

# 对任何提示回答“是”。
# 参见 JupyterApp.answer_yes
# c.ExtensionApp.answer_yes = False

# 配置文件的完整路径。
# 参见 JupyterApp.config_file
# c.ExtensionApp.config_file = ''

# 指定加载的配置文件。
# 参见 JupyterApp.config_file_name
# c.ExtensionApp.config_file_name = ''

# 默认值: ''
# c.ExtensionApp.default_url = ''
# 生成默认配置文件
# c.ExtensionApp.generate_config = False

# 添加到服务器的处理程序
# c.ExtensionApp.handlers = []

# 日志格式化程序使用的日期格式
# c.ExtensionApp.log_datefmt = '%Y-%m-%d %H:%M:%S'

# 日志格式模板
# c.ExtensionApp.log_format = '[%(name)s]%(highlevel)s %(message)s'

# 设置日志级别
# c.ExtensionApp.log_level = 30

# 日志配置
# c.ExtensionApp.logging_config = {}

# 启动后是否在浏览器中打开
# c.ExtensionApp.open_browser = False

# 传递给服务器的设置
# c.ExtensionApp.settings = {}

# 将配置输出到标准输出（而不是启动应用程序）
# c.ExtensionApp.show_config = False

# 将配置以 JSON 格式输出到标准输出（而不是启动应用程序）
# c.ExtensionApp.show_config_json = False

# 用于提供静态文件的路径
# c.ExtensionApp.static_paths = []

# 扩展的静态资源 URL 前缀
# c.ExtensionApp.static_url_prefix = ''

# 用于提供 Jinja 模板的路径
# c.ExtensionApp.template_paths = []

# LabServerApp 配置
# ------------------------------------------------------------------------------
# 允许的扩展列表的 URI
# c.LabServerApp.allowed_extensions_uris = ''

# 自动回答所有提示为 "是"
# c.LabServerApp.answer_yes = False

# 应用程序设置目录
# c.LabServerApp.app_settings_dir = ''

# 应用程序的 URL 路径
# c.LabServerApp.app_url = '/lab'

# 被阻止的扩展列表的 URI
# c.LabServerApp.blocked_extensions_uris = ''

# 是否在服务器上缓存文件（开发模式下应为 False）
# c.LabServerApp.cache_files = True

# 配置文件的完整路径
# c.LabServerApp.config_file = ''

# 配置文件名称
# c.LabServerApp.config_file_name = ''

# 复制路径时是否使用绝对路径
# c.LabServerApp.copy_absolute_path = False

# 额外搜索 JupyterLab 扩展的路径
# c.LabServerApp.extra_labextensions_path = []

# 生成默认配置文件
# c.LabServerApp.generate_config = False

# 添加到服务器的处理程序
# c.LabServerApp.handlers = []

# 传递给 Jinja2 环境的选项
# c.LabServerApp.jinja2_options = {}

# 标准 JupyterLab 扩展路径
# c.LabServerApp.labextensions_path = []

# 联邦 JupyterLab 扩展的 URL
# c.LabServerApp.labextensions_url = ''

# 列表刷新间隔（秒）
# c.LabServerApp.listings_refresh_seconds = 3600

# 用于 HTTP 请求的选项
# c.LabServerApp.listings_request_options = {}

# 列表 URL
# c.LabServerApp.listings_url = ''

# 日志格式化程序使用的日期格式
# c.LabServerApp.log_datefmt = '%Y-%m-%d %H:%M:%S'

# 日志格式模板
# c.LabServerApp.log_format = '[%(name)s]%(highlevel)s %(message)s'

# 设置日志级别
# c.LabServerApp.log_level = 30

# 是否自动启动内核
# c.LabServerApp.notebook_starts_kernel = True

# 启动后是否在浏览器中打开
# c.LabServerApp.open_browser = False

# 设置模式的目录
# c.LabServerApp.schemas_dir = ''

# 传递给服务器的设置
# c.LabServerApp.settings = {}

# 设置处理程序的 URL 路径
# c.LabServerApp.settings_url = ''

# 将配置输出到标准输出（而不是启动应用程序）
# c.LabServerApp.show_config = False

# 将配置以 JSON 格式输出到标准输出（而不是启动应用程序）
# c.LabServerApp.show_config_json = False

# 本地静态文件的目录
# c.LabServerApp.static_dir = ''

# 用于提供静态文件的路径
# c.LabServerApp.static_paths = []

# 扩展的静态资源 URL 前缀
# c.LabServerApp.static_url_prefix = ''

# 用于提供 Jinja 模板的路径
# c.LabServerApp.template_paths = []

# 应用程序模板目录
# c.LabServerApp.templates_dir = ''

# 主题目录
# c.LabServerApp.themes_dir = ''

# 主题 URL
# c.LabServerApp.themes_url = ''

# 翻译处理程序的 URL 路径
# c.LabServerApp.translations_api_url = ''

# 工作区 API 的 URL 路径
# c.LabServerApp.workspaces_api_url = ''

# 保存工作区的目录
# c.LabServerApp.workspaces_dir = ''

# ServerApp 配置
# ------------------------------------------------------------------------------
# 设置 Access-Control-Allow-Credentials: true 头
# c.ServerApp.allow_credentials = False

# 是否允许外部内核
# c.ServerApp.allow_external_kernels = False

# 设置 Access-Control-Allow-Origin 头
# c.ServerApp.allow_origin = ''

# 是否允许用户以 root 身份运行服务器
# c.ServerApp.allow_root = False

# 自动回答所有提示为 "是"
# c.ServerApp.answer_yes = False

# 基础 URL
# c.ServerApp.base_url = '/'

# 启动后是否在浏览器中打开
# c.ServerApp.browser = ''

# SSL/TLS 证书文件的完整路径
# c.ServerApp.certfile = ''

# SSL/TLS 客户端认证的证书颁发机构文件
# c.ServerApp.client_ca = ''

# 配置文件的完整路径
# c.ServerApp.config_file = ''

# 配置文件名称
# c.ServerApp.config_file_name = ''

# 默认 URL 重定向
# c.ServerApp.default_url = '/'

## 禁用跨站请求伪造（CSRF）保护
## Jupyter Server 默认包含跨站请求伪造保护，要求 API 请求必须：
## - 来自由该服务器提供的页面（通过 XSRF cookie 和 token 验证），或
## - 使用 token 进行身份验证
## 一些匿名计算资源可能希望完全禁用身份验证和安全检查，需明确了解其含义。
## 默认值: False
# c.ServerApp.disable_check_xsrf = False

## 如果 allow_external_kernels 为 True，则用于查找外部内核连接文件的目录。
## 默认值为 Jupyter runtime_dir/external_kernels。确保此目录中没有多余的连接文件，以避免不必要的内核管理器创建。
## 默认值: None
# c.ServerApp.external_connection_dir = None

## 应优先加载的处理程序（高于默认服务）。
## 默认值: []
# c.ServerApp.extra_services = []

## 提供额外的路径以搜索静态文件。
## 这允许添加 JavaScript/CSS 文件，或覆盖 IPython 中的单个文件。
## 默认值: []
# c.ServerApp.extra_static_paths = []

## 提供额外的路径以搜索 Jinja 模板。
## 可用于覆盖 jupyter_server.templates 中的模板。
## 默认值: []
# c.ServerApp.extra_template_paths = []

## 启动应用程序时打开指定的文件。
## 默认值: ''
# c.ServerApp.file_to_run = ''

## 打开文件时的 URL 前缀。
## 默认值: 'notebooks'
# c.ServerApp.file_url_prefix = 'notebooks'

## 生成默认配置文件。
## 默认值: False
# c.ServerApp.generate_config = False

## 身份提供者类。
## 默认值: 'jupyter_server.auth.identity.PasswordIdentityProvider'
# c.ServerApp.identity_provider_class = 'jupyter_server.auth.identity.PasswordIdentityProvider'

## Jupyter Server 监听的 IP 地址。
## 默认值: 'localhost'
# c.ServerApp.ip = 'localhost'

## 提供给 Jinja 环境的额外参数。
## 默认值: {}
# c.ServerApp.jinja_environment_options = {}

## 渲染 Jinja 模板时提供的额外变量。
## 默认值: {}
# c.ServerApp.jinja_template_vars = {}

## 用于加载 Jupyter Server 扩展的 Python 模块字典。
## 默认值: {}
# c.ServerApp.jpserver_extensions = {}

## 使用的内核管理器类。
## 默认值: 'jupyter_server.services.kernels.kernelmanager.MappingKernelManager'
# c.ServerApp.kernel_manager_class = 'jupyter_server.services.kernels.kernelmanager.MappingKernelManager'

## 使用的内核规范管理器类。
## 默认值: 'builtins.object'
# c.ServerApp.kernel_spec_manager_class = 'builtins.object'

## 使用的内核 WebSocket 连接类。
## 默认值: 'jupyter_server.services.kernels.connection.base.BaseKernelWebsocketConnection'
# c.ServerApp.kernel_websocket_connection_class = 'jupyter_server.services.kernels.connection.base.BaseKernelWebsocketConnection'

## 私钥文件的完整路径，用于 SSL/TLS。
## 默认值: ''
# c.ServerApp.keyfile = ''

## 允许的本地主机名列表，当 allow_remote_access 为 False 时使用。
## 默认值: ['localhost']
# c.ServerApp.local_hostnames = ['localhost']

## 日志格式中的日期格式。
## 默认值: '%Y-%m-%d %H:%M:%S'
# c.ServerApp.log_datefmt = '%Y-%m-%d %H:%M:%S'

## 日志格式模板。
## 默认值: '[%(name)s]%(highlevel)s %(message)s'
# c.ServerApp.log_format = '[%(name)s]%(highlevel)s %(message)s'

## 设置日志级别。
## 默认值: 30
# c.ServerApp.log_level = 30

## 使用的登录处理程序类。
## 默认值: 'jupyter_server.auth.login.LegacyLoginHandler'
# c.ServerApp.login_handler_class = 'jupyter_server.auth.login.LegacyLoginHandler'

## 使用的注销处理程序类。
## 默认值: 'jupyter_server.auth.logout.LogoutHandler'
# c.ServerApp.logout_handler_class = 'jupyter_server.auth.logout.LogoutHandler'

## 客户端请求体的最大允许大小（以字节为单位）。
## 默认值: 536870912
# c.ServerApp.max_body_size = 536870912

## 缓冲区管理器允许的最大内存大小（以字节为单位）。
## 默认值: 536870912
# c.ServerApp.max_buffer_size = 536870912

## 是否在启动后打开浏览器。
## 默认值: False
# c.ServerApp.open_browser = False

## 服务器监听的端口。
## 默认值: 0
# c.ServerApp.port = 0

## 如果指定端口不可用，尝试的额外端口数量。
## 默认值: 50
# c.ServerApp.port_retries = 50

## 是否显示关闭 Jupyter Server 的控件（如菜单项或按钮）。
## 默认值: True
# c.ServerApp.quit_button = True

## 服务器关闭前的空闲超时时间（以秒为单位）。0 表示禁用自动关闭。
## 默认值: 0
# c.ServerApp.shutdown_no_activity_timeout = 0

## UNIX 套接字的权限模式（默认: 0600）。
## 默认值: '0600'
# c.ServerApp.sock_mode = '0600'

## 是否信任由上游反向代理发送的 X-Scheme/X-Forwarded-Proto 和 X-Real-Ip/X-Forwarded-For 头信息。
## 默认值: False
# c.ServerApp.trust_xheaders = False

## 是否禁用通过重定向文件启动浏览器。
## 默认值: True
# c.ServerApp.use_redirect_file = True

## 指定启动服务器时的浏览器打开方式。
## - 2：新标签页
## - 1：新窗口
## - 0：现有窗口
## 默认值: 2
# c.ServerApp.webbrowser_open_new = 2

## 配置 WebSocket 的压缩选项。
## 默认值: None
# c.ServerApp.websocket_compression_options = None

## 配置 WebSocket 的 ping 间隔时间（以秒为单位）。
## 默认值: 0
# c.ServerApp.websocket_ping_interval = 0

## 配置 WebSocket 的 ping 超时时间（以秒为单位）。
## 默认值: 0
# c.ServerApp.websocket_ping_timeout = 0