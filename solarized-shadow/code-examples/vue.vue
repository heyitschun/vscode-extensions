<template>
  <div id="product-list-two">
    <ul>
      <li v-for="product in saleProducts" :key="product.name">
        <span class="name">
          {{ product.name }}
        </span>
      </li>
    </ul>
  </div>
</template>

<script>
export default {
  name: "ProductListTwo",
  computed: {
    products() {
      return this.$store.state.products;
    },
    saleProducts() {
      return this.$store.getters.saleProducts;
    }
  }
}
</script>

<style scoped>
#product-list-two{
  background: #D1E4FF;
  box-shadow: 1px 2px 3px rgba(0,0,0,0.2);
  margin-bottom: 30px;
  padding: 10px 20px;
}
.price{
  font-weight: bold;
  color: #860CE8;
  display: block;
}
</style>
