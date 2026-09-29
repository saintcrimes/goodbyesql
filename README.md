# goodbyesql

### Simplify SQLAlchemy. Say goodbye to repetitive database code.

`goodbyesql` is a lightweight Python library built on top of **SQLAlchemy** that helps backend developers reduce repetitive database boilerplate.

It provides a simple interface for working with common SQLAlchemy operations while keeping SQLAlchemy underneath.

## ✨ Features

* 🐍 Built for Python backend applications
* 🗄️ Built on top of SQLAlchemy
* ⚡ Simplifies common database operations
* 🧹 Reduces repetitive SQLAlchemy boilerplate
* ⚙️ Configurable database setup
* 🔌 Custom session provider support

## 📦 Installation

```bash
pip install goodbyesql
```

## 🚀 Quick Start

```python
from goodbyesql import GoodbyeSQL, GoodbyeSQLConfig

config = GoodbyeSQLConfig(
    # your configuration
)

db = GoodbyeSQL(config)
```

`GoodbyeSQL` provides a higher-level interface for common database operations while using SQLAlchemy internally.

## 🔧 Session Provider

`goodbyesql` also allows you to configure your own SQLAlchemy session provider:

```python
from goodbyesql import set_session_provider

set_session_provider(your_session_provider)
```

This makes it possible to integrate `goodbyesql` into existing backend architectures where database sessions are already managed by the application.

## 🏗️ How It Works

`goodbyesql` is not a replacement for SQLAlchemy.

Instead, it provides a convenient abstraction on top of it:

```text
┌─────────────────────┐
│   Your Application  │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│     goodbyesql      │
│  Simple DB API      │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      SQLAlchemy     │
└──────────┬──────────┘
           │
           ▼
┌─────────────────────┐
│      Database       │
└─────────────────────┘
```

The goal is simple:

> **Write less repetitive database code and focus more on your application.**

## 🎯 Who is it for?

`goodbyesql` is designed primarily for **Python backend developers** who use SQLAlchemy and want a simpler way to handle common database functionality.

It can be especially useful in projects such as:

* REST APIs
* FastAPI applications
* Backend services
* Automation systems
* Microservices
* Other Python applications using SQLAlchemy

## 📚 Public API

### `GoodbyeSQL`

The main class used to work with `goodbyesql`.

```python
from goodbyesql import GoodbyeSQL
```

### `GoodbyeSQLConfig`

Configuration for `GoodbyeSQL`.

```python
from goodbyesql import GoodbyeSQLConfig
```

### `set_session_provider`

Configure the session provider used by `goodbyesql`.

```python
from goodbyesql import set_session_provider
```

## 🚧 Project Status

`goodbyesql` is currently under active development.

The API may change in future releases as the project evolves.

Feedback, issues, and contributions are welcome.

## 🤝 Contributing

Contributions are welcome!

Feel free to open an issue or submit a pull request if you have an idea, improvement, or bug fix.

## 📄 License

See the `LICENSE` file for license information.
