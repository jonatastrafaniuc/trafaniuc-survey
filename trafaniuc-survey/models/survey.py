import enum
from datetime import datetime
from ..ext.database import db, Doc


class SurveyStatus(enum.Enum):
    draft = 'draft'
    opened = 'open'
    closed = 'closed'


class SurveyQuestionScheme(enum.Enum):
    exclusive = 'exclusive'


class Survey(Doc):
    def __init__(self, owner: str, title: str, status: SurveyStatus, questions: list, doc: dict = None):
        if doc:
            super().__init__(doc)
        else:
            super().__init__({
                'owner': owner,
                'created_on': datetime.utcnow(),
                'updated_on': datetime.utcnow(),
                'title': title,
                'status': status.value,
                'questions': [doc.get_doc() for doc in questions]
            })

    def set_update_time(self):
        self.doc['updated_on'] = datetime.utcnow()

    @classmethod
    def get_owner_drafts(cls, owner: str, skip: int, limit: int):
        filters = {
            '$and': [{
                'owner': owner,
                'status': SurveyStatus.draft.value
            }]
        }
        projection = ['owner','created_on','updated_on','title']
        return list(db.db.surveys.find(
            filter=filters,
            projection=projection,            
            skip=0,
            limit=20)
        )


class SurveyQuestion(Doc):
    def __init__(self, text: str, scheme: SurveyQuestionScheme, options: list, doc: dict = None):
        if doc:
            super().__init__(doc)
        else:
            super().__init__({
                'text': text,
                'scheme': scheme.value,
                'options': [doc.get_doc() for doc in options]
            })


class SurveyQuestionOption(Doc):
    def __init__(self, order: int, text: str, doc: dict = None):
        if doc != None:
            super().__init__(doc)
        else:
            super().__init__({
                'order': order,
                'text': text
            })
