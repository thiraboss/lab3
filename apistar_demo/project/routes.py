from apistar import Include, Route
from apistar.docs import docs_routes
from apistar.statics import static_routes
from project.views import welcome , students,students_get




routes = [
    Route('/students/id/{index}','GET',students_get),
    Route('/students','GET',students),
    Route('/', 'GET', welcome),
    Include('/docs', docs_routes),
    Include('/static', static_routes),

]