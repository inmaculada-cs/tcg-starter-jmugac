[![Open in Visual Studio Code](https://classroom.github.com/assets/open-in-vscode-c66648af7eb3fe8bc4f294546bfd86ef473780cde1dea487d3c4ff354943c9ae.svg)](https://classroom.github.com/online_ide?assignment_repo_id=8047111&assignment_repo_type=AssignmentRepo)
# tcg-backend

## Prerrequisitos

* Python >= 3.8, < 3.11
* Tener instalado [Poetry](https://python-poetry.org/)

## Instalación

```bash
poetry install
```

## Ejecución

Desarrollo:

```bash
poetry run uvicorn app.main:app --reload
```