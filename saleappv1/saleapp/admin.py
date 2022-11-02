from saleapp.models import Category, Product
from saleapp import db, app
from flask_admin import Admin, expose, BaseView
from flask_admin.contrib.sqla import ModelView


class ProductView(ModelView):
    column_searchable_list = ["name", "description"]
    column_filters = ["name", "price"]
    can_view_details = True
    can_export = True
    column_exclude_list = ["image"]
    column_labels = {
        'name': 'ten san pham',
        'description': 'mo ta',
        'price': 'gia'
    }


class StatsView(BaseView):
    @expose("/")
    def index(self):
        return self.render("admin/stats.html")


admin = Admin(app=app, name = "Quan tri ban hang", template_mode="bootstrap4")
admin.add_view(ModelView(Category, db.session, name="Danh muc"))
admin.add_view(ProductView(Product, db.session, name="San pham"))
admin.add_view(StatsView(name = "Thong ke"))