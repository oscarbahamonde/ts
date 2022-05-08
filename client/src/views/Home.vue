<template>
  <div class="flex flex-row">
    <iframe
      title="HHMC en Huancayo"
      src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2Fhiphopmovimientoycultura%2Fposts%2F3171445223144726&show_text=false&width=500"
      width="500"
      height="496"
      class="fb-post"
      scrolling="yes"
      frameborder="0"
      allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"
    />
    <div class="py-16 pr-16">
      En setiembre del 2021, realizamos nuestro primer viaje como HHMC a la
      ciudad de Huaral, participando como agrupación Hip Hop en la Competencia
      Nacional de Ajedrez realizada por la Federación Nacional de Ajedrez, con
      el apoyo del Grupo Baldeón. En esta oportunidad, participaremos este
      sábado 05 de marzo, del festival clandestino
      <strong>"Wayki Fest"</strong>, en la ciudad de Huancayo. Este evento es
      organizado periódicamente por <strong>HardCorp Estudios</strong>, donde
      por primera vez tendremos el gusto de compartir los temas de
      <strong>Snare Lee</strong>, <strong>Trece Disociativo</strong>,
      <strong>Tettimo</strong> &
      <strong>Joselo Mc.</strong>
      <h2 class="my-4 font-script">En Tarima:</h2>
      <button
        v-for="(data, index) in data"
        class="badge font-sans mx-2 w-32 my-1 rounded-xl"
      >
        {{ data }}
      </button>
    </div>
  </div>
  <div class="flex flex-row my-16 pb-24">
    <iframe
      title="chalex"
      class="fb-post"
      src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2Fhiphopmovimientoycultura%2Fposts%2F3200975763525005&show_text=false&width=500"
      width="500"
      height="498"
      style="border: none; overflow: hidden"
      scrolling="no"
      frameborder="0"
      allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"
    ></iframe>
    <iframe
      title="negrata wanka"
      class="fb-post"
      src="https://www.facebook.com/plugins/post.php?href=https%3A%2F%2Fwww.facebook.com%2FVERSOFENES%2Fphotos%2Fa.2146362622143865%2F4857203411059759%2F%3Ftype%3D3&show_text=false&width=500"
      width="500"
      height="497"
      style="border: none; overflow: hidden"
      scrolling="no"
      frameborder="0"
      allow="autoplay; clipboard-write; encrypted-media; picture-in-picture; web-share"
    ></iframe>
  </div>
</template>
<style>
.fb-post {
  @apply px-8 bg-black scale-75 rounded-lg shadow-2xl mx-8 my-2 z-10;
}
</style>

<script setup>
const data = [
  "THE SHOOT",
  "ILEGAL MAN",
  "UYARIKUAY LL",
  "AWKA Y",
  "TRAZÓ",
  "VERSÓFENES",
  "BUDA NIGROM",
  "SUPAY",
  "BLAZ HOP",
  "JH ROOTS",
  "LLEGENDARIOS",
  "WANKLAN",
  "HPV Hard",
  "EL PHLEPS",
  "EL BETTER 999",
  "JF ETERNO",
  "EL PLENO",
  "EL ZERMITAÑO",
  "CAMERON 420",
  "POETIC STREET",
  "ICA FLOW TRFIK",
  "TÁCITO BOICOT",
];
</script>
