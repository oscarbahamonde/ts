<template>
<form action="/api/contact/send" method="POST" enctype="application/json" class="flex flex-col px-32 mx-32 pb-24"
@submit.prevent="sendMessage"
>
<label for="name" class="contact_form-label"> Nombre</label>
<input type="text" class="contact_form-input" name="name" id="name" placeholder="Nombre" required v-model="name">
<label for="email" class="contact_form-label">Email</label>
<input type="email" class="contact_form-input" name="email" id="email" placeholder="Email" required v-model="email">
<label for="message" class="contact_form-label">Mensaje</label>
<textarea name="message" id="message" placeholder="Mensaje" rows="4" required  v-model="message" class="contact_form-textarea"></textarea>
<input type="submit" class="contact_form-submit" value="Enviar">
</form>
<p>{{response}}</p>
</template>
<script>
import { ref } from 'vue'
export default {
    name: 'Contact',
    data() {
        return {
            name: '',
            email: '',
            message: '',
            response: ''
        }
    },
    methods: {
        sendMessage() {
            const data = {
                name: this.name,
                email: this.email,
                message: this.message
            }
            fetch('/api/contact/send', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body: JSON.stringify(data)
            }).then(res => res.json())
            .then(data => {
                this.response = data
            })
        }
    }
}
</script>