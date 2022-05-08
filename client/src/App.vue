<template>
<Navbar />
<div class="con pt-32 p-8 bg-base-300">
<router-view></router-view>
</div>
<Footer />
</template>
<script setup>
import Navbar from './layouts/Navbar.vue'
import Footer from './layouts/Footer.vue'
</script>