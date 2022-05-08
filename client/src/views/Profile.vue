<script setup>
import { ref, onBeforeMount, onMounted } from "vue";
import { useRoute } from "vue-router";
const route = useRoute();
const id = ref(route.query.id);
const user = ref(null);
const text = ref(null);
const background = ref(null);
const card = ref(null);
const buttons = ref(null);
const loading = ref(false);
if (id.value == null || id.value == undefined || id.value == "") {
  user.value = JSON.parse(localStorage.getItem("user"));
  } else {
  onBeforeMount(async () => {
    user.value = await fetch("/api/auth/token?code=" + id.value, {
      method: "POST",
    }).then((res) => res.json());
    localStorage.setItem("user", JSON.stringify(user.value));
  });
  }
onMounted(() => {
  user.value = JSON.parse(localStorage.getItem("user"));
});
const logout = () => {
  localStorage.removeItem("user");
  user.value = null;
  window.location.href = "/";
};
const login = () => {
  window.location.href =
    "https://obm.auth.us-east-1.amazoncognito.com/login?client_id=7rts72q3ki6tjki5uk0jm3ujd7&response_type=code&scope=email+openid&redirect_uri=https://smartpro.solutions/auth/token";
};
const image = ref(null);
const description = ref(null)
const handler = (e) => {
  e.preventDefault();
  image.value = e.target.files[0];
};

const url = ref(null);
const upload = () => {
  const formData = new FormData();
  formData.append("file", image.value);
  fetch(`/api/drive/upload?id=${id.value}`, {
    method: "POST",
    body: formData,
  })
    .then((res) => res.json())
    .then((data) => {
      url.value = data.url;
    });
};

const updateProfile = () => {
  loading.value = true;
  fetch(`/api/auth/user/update`, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
    },
    body: {
      id: id.value,
      username: user.value.username,
      email: user.value.email,
      colors:{
        background: background.value,
        text: text.value,
        card: card.value,
        buttons: buttons.value
      },
      image: url.value,
      description: description.value
    }
})
    .then((res) => res.json())
    .then((data) => {
      loading.value = false;
    });
};


const updateDescription = () => {
  description.value = document.getElementById("description").value;
}
</script>

<template>
  <div class="flex flex-row" v-if="user">
    <div class="w-1/2">
      <p>{{ user.username }}</p>
      <p>{{ user.email }}</p>
      <h1>Edita tu perfil</h1>
      <input type="color" v-model="text" />
      <input type="color" v-model="background" />
      <input type="color" v-model="card" />
      <input type="color" v-model="buttons" />
      <textarea 
      :v-model="description"
        placeholder="Describe tu perfil"
        id="description"
        rows="5"
        cols="50"
        @keyup.enter="updateDescription"
      
      
       />
      <div>
        <input type="file" accept="image/*" @change="handler" />
      </div>
      <button @click="upload">Upload</button>
    </div>
    <div
      class="w-1/2 p-8"
      :style="{ backgroundColor: background, color: text }"
    >
      <div class="avatar">
        <div class="w-24 rounded-full">
          <img
            :src="url"
            class="avatar online"
            :alt="user.username"
            width="100"
            height="100"
          />
        </div>
      </div>
      <div class="card" :style="{ backgroundColor: card }">
        <div class="card-body">
          <h5 class="card-title">{{ user.username }}</h5>
          <p class="card-text">{{ user.email }}</p>
          <p class="card-text">{{ description }}</p>
        </div>
      </div>
      <button
        @click="logout"
        class="btn btn-primary my-8"
        :style="{ backgroundColor: buttons, color: text }"
      >
        Logout
      </button>
    </div>
  </div>
  <div v-else>
    <button @click="login">Login</button>
  </div>
  <button 
    @click="updateProfile"
  >Publicar</button>
</template>
