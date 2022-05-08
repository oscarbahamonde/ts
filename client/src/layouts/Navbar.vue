<template>
<div class="navbar bg-white shadow-lg fixed" style="z-index: 998;">
<div class="flex-1"><router-link to="/">
<img alt="Hip Hop Movimiento Cultural" src="/favicon.png"  class="logo"/>
</router-link></div>
<ul class="menu menu-horizontal">
<li><router-link to="/">Inicio</router-link></li>
<li><router-link to="/about">Acerca de</router-link></li>
<li><router-link to="/contact">Contacto</router-link></li>
<li><router-link to="/profile"><button class="btn-circle btn-outline h-12 w-12">
<i class="mdi-account text-2xl"></i>
</button></router-link></li>
</ul>
</div>
</template>