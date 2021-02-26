<template>
  <q-page padding class="flex flex-center">
    <q-card square style="width: 400px; padding:50px">
      <q-card-section>
        <div class="text-h6">
          <!-- {{ $t('auth.register.register') }} -->
          REGISTER
        </div>
      </q-card-section>

      <q-card-section>
        <q-input
          id="email"
          v-model.trim="data.email"
          type="text"
          label="Email"
          bottom-slots
          autofocus
          :rules="[(val) => !!val || 'Email is missing', isValidEmail]"
        />
        <q-input
          v-model.trim="data.first_name"
          type="text"
          label="First Name"
        />
        <q-input v-model.trim="data.last_name" type="text" label="Last Name" />
        <q-input
          id="password"
          v-model="data.password"
          type="password"
          label="Password"
        />
        <!--         <q-input
          id="repeatPassword"
          v-model="data.repeatPassword"
          type="password"
          :label="$t('auth.register.repeat_password')"
          bottom-slots
          required
          :error="$v.data.repeatPassword.$error"
          :error-message="$t('auth.register.errors.password_match')"
        /> -->
      </q-card-section>
      <q-card-actions>
        <q-btn
          color="primary"
          :loading="loading"
          label="Register"
          @click="register"
        />
      </q-card-actions>
    </q-card>
  </q-page>
</template>

<style></style>

<script>
// import { email, required, sameAs, minLength } from 'vuelidate/lib/validators'

const minPasswordLength = 8;

export default {
  name: "Register",
  data() {
    return {
      data: {
        first_name: "",
        last_name: "",
        email: "",
        password: "",
        repeatPassword: "",
      },
      loading: false,
      minPasswordLength: minPasswordLength,
    };
  },
  methods: {
    isValidEmail(val) {
      const emailPattern = /^(?=[a-zA-Z0-9@._%+-]{6,254}$)[a-zA-Z0-9._%+-]{1,64}@(?:[a-zA-Z0-9-]{1,63}\.){1,8}[a-zA-Z]{2,63}$/;
      return emailPattern.test(val) || "Invalid email";
    },
    register() {
      // this.$v.data.$touch()
      // if (!this.$v.data.$error) {
      //   this.$q.dialog({
      //     message: this.$t('auth.register.check_email', { email: this.data.email }),
      //     cancel: true
      //   }).onOk(() => {
      //     this.loading = true
      //     this.$auth.register(this.data).then(() => {
      //       this.$q.dialog({
      //         message: this.$t('auth.register.account_created')
      //       }).onOk(data => {
      //         this.$router.push('/login')
      //       })
      //     }).catch((error) => {
      //       if (error.response) {
      //         if (error.response.status === 422) {
      //           this.$q.dialog({
      //             message: this.$t('auth.register.invalid_data')
      //           })
      //         } else if (error.response.status === 409) {
      //           this.$q.dialog({
      //             message: this.$t('auth.register.already_registered')
      //           })
      //         } else {
      //           console.error(error)
      //         }
      //       }
      //     }).finally(() => {
      //       this.loading = false
      //     })
      //   })
      // }
    },
  }, // End of methods
  // validations: {
  //   data: {
  //     name: { required },
  //     email: {
  //       required,
  //       email
  //     },
  //     password: {
  //       required,
  //       minLength: minLength(minPasswordLength)
  //     },
  //     repeatPassword: {
  //       sameAsPassword: sameAs('password')
  //     }
  //   }
  // }
};
</script>
