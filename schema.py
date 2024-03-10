#schema.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey, DateTime, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship

engine = create_engine('sqlite:///example.db', echo=True)
Base = declarative_base()

class ProductCategory(Base):
    _tablename_ = 'product_category'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    created_at = Column(DateTime)
    modified_at = Column(DateTime)
    deleted_at = Column(DateTime)

class Product(Base):
    _tablename_ = 'product'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    description = Column(Text)
    category_id = Column(Integer, ForeignKey('product_category.id'))
    category = relationship("ProductCategory")
    created_at = Column(DateTime)
    modified_at = Column(DateTime)
    deleted_at = Column(DateTime)

Base.metadata.create_all(engine)
