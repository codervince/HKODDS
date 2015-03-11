# -*- coding: utf-8 -*-

"""The application's model objects"""
from models.meta import Session, Base
from models import meta

meta.metadata = Base.metadata

def init_model(engine):
	"""Call me before using any of the tables or classes in the model"""
	Session.configure(bind=engine, autocommit = True)

def setup_model(model, metadata, **p):
	pass
