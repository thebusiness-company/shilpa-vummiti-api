from rest_framework import serializers
from .models import Category, Product, ProductImage, Cart, CartItem, Wishlist

# --- Category ---
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

# --- Product & Images ---
class ProductImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductImage
        fields = ['images']

class ProductSerializer(serializers.ModelSerializer):
    category_name = serializers.CharField(source='category.name', read_only=True)
    images = ProductImageSerializer(many=True, read_only=True)

    class Meta:
        model = Product
        fields = '__all__'

# --- Cart Items ---
class CartItemSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)
    cart = serializers.PrimaryKeyRelatedField(read_only=True)  # Avoid nesting CartSerializer here

    class Meta:
        model = CartItem
        fields = ["id", "quantity", "product", "product_size","cart"]

    def update(self, instance, validated_data):
        instance.quantity = validated_data.get('quantity', instance.quantity)
        instance.product_size = validated_data.get('product_size', instance.product_size)
        instance.save()
        return instance

# --- Cart ---
class CartSerializer(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)

    class Meta:
        model = Cart
        fields = ["id", "cart_code", "created_at", "modified_at", "items"]

# --- Wishlist ---
class WishlistSerializer(serializers.ModelSerializer):
    product = ProductSerializer(read_only=True)

    class Meta:
        model = Wishlist
        fields = ['id', 'product', 'added_at']
        
class SimpleCartSerializer(serializers.ModelSerializer):
    num_of_items = serializers.SerializerMethodField()

    class Meta:
        model = Cart
        fields = ["id", "cart_code", "num_of_items"]

    def get_num_of_items(self, cart):
        return sum(item.quantity for item in cart.items.all())
