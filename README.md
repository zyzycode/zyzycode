<p align="center">
  <img src="https://raw.githubusercontent.com/zyzycode/zyzycode/main/assets/header.svg" width="100%" alt="zyzycode — Backend systems. Desktop apps. Playable worlds." />
</p>

<p align="center">
  <a href="#проекты">Проекты</a> &nbsp; / &nbsp;
  <a href="#стек">Стек</a> &nbsp; / &nbsp;
  <a href="https://github.com/zyzycode?tab=repositories">Все репозитории</a>
</p>

## Привет, я zyzycode

Пишу на **Python и TypeScript**. Разрабатываю серверные системы, desktop-приложения и игры: от очередей сообщений и API до интерфейсов и игровой логики.

Мне интересно, как устроен продукт целиком: что видит пользователь, как проходят данные и что происходит, когда что-то идёт не по плану.

## Проекты

### [Project Wisp ↗](https://github.com/zyzycode/project_wisp)

**AI-компаньон, который живёт на рабочем столе.**

Desktop-приложение с локальной памятью и offline-first runtime. Electron и React на клиенте, Python/FastAPI на сервере. Локальная работа и внешние AI-вызовы разделены границами процессов.

`Electron` `React` `TypeScript` `Python` `FastAPI`

---

### [Async Payments Service ↗](https://github.com/zyzycode/async-payments-service)

**Платёжный запрос сейчас. Обработка и webhook — асинхронно.**

Сервис с эмуляцией платёжного шлюза: идемпотентность запросов, transactional outbox, очередь RabbitMQ, повторы с backoff и DLQ. Архитектура Ports & Adapters отделяет бизнес-логику от инфраструктуры.

`Python` `FastAPI` `PostgreSQL` `SQLAlchemy` `RabbitMQ` `Docker`

---

### [Пепельный путь ↗](https://github.com/zyzycode/zombz-like-starter)

**Roguelike: шесть уровней, три биома и один шанс дойти до босса.**

Одиночная top-down игра в стадии альфы: бой, магия, навыки, экипировка и постоянные улучшения между забегами. Игровая симуляция отделена от Phaser, React и браузерного хранилища.

`TypeScript` `Phaser` `React` `Vite`

## Стек

| Направление | Технологии из проектов |
| :--- | :--- |
| Backend | Python · FastAPI · Pydantic · SQLAlchemy · Alembic |
| Данные и сообщения | PostgreSQL · RabbitMQ · FastStream |
| Интерфейсы и desktop | TypeScript · React · Electron · Vite |
| Игры | Phaser · игровая симуляция · системы прогрессии |
| Инструменты | Git · Docker Compose · pytest |

<br />

<p align="center"><sub>От серверной логики до миров, в которые можно играть.</sub></p>
