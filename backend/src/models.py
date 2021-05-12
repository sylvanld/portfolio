from typing import List
from pydantic import BaseModel
from datetime import datetime
from dataclasses import dataclass


class APIModel(BaseModel):
    class Config:
        orm_mode = True


class IndexArticle(BaseModel):
    code: str
    title: str
    published: bool = False
    created_at: datetime
    updated_at: datetime


class FullArticle(IndexArticle):
    content: str


class IndexData(BaseModel):
    articles: List[IndexArticle] = []


class EditArticle(BaseModel):
    code: str 
    title: str
    content: str


class Repository(APIModel):
    id: int
    name: str
    full_name: str
    description: str = None
    topics: List[str] = []

    license: str = None
    forked: bool
    private: bool

    open_issues_count: int
    commits_count: int
    stargazers_count: int
    watchers_count: int

    repository_url: str
    showcase_url: str = None

    created_at: datetime
    updated_at: datetime
