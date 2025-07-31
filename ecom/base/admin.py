from django.contrib import admin
from .models import *

admin.site.register(Profile)
admin.site.register(ShippingAddress)
admin.site.register(Category)
admin.site.register(Product)
admin.site.register(ProductImage)
admin.site.register(ProductReview)
admin.site.register(SizeVariant)
admin.site.register(ColorVariant)
admin.site.register(Wishlist)
admin.site.register(Coupon)
admin.site.register(Cart)
admin.site.register(CartItem)
admin.site.register(Order)
admin.site.register(OrderItem)
