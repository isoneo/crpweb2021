<template>
  <q-layout>
    <q-page-container>
      <q-page class="flex flex-center">
        <div
          id="particles-js"
          :class="$q.dark.isActive ? 'dark_gradient' : 'normal_gradient'"
        ></div>
        <q-card
          class="login-form"
          v-bind:style="
            $q.platform.is.mobile ? { width: '80%' } : { width: '30%' }
          "
        >
          <!-- <q-img src="/statics/images/pharmacy.jpg"></q-img> -->
          <q-card-section>
<!--             <q-avatar
              size="74px"
              class="absolute"
              style="top: 0;right: 25px;transform: translateY(-50%);"
            >
              
            </q-avatar> -->
            <div class="row no-wrap items-center">
              <div class="col text-h6 ellipsis">
                Log in to Zonkey
              </div>
            </div>
          </q-card-section>
          <q-card-section>
            <q-form class="q-gutter-md">
              <q-input
                filled
                v-model="loginForm.username"
                label="Email"
                lazy-rules
              />

              <q-input
                type="password"
                filled
                v-model="loginForm.password"
                label="Password"
                lazy-rules
              />

              <div>
                <q-btn
                  label="Login"
                  to="/"
                  type="button"
                  color="primary"
                  @click="attemptLogin"
                />
                <q-btn
                class = "float-right"
                  label="Register"                
                  type="button"
                  color="orange"
                  @click="sendToRegister"
                />

<!--                 <a
                  style="font-size: 30px;"
                  class="float-right"
                  href="https://github.com/sponsors/mayank091193"
                  target="_blank"
                  title="Donate"
                  ><i class="fas fa-heart" style="color: #eb5daa"></i
                ></a> -->
              </div>
            </q-form>
          </q-card-section>
        </q-card>
      </q-page>
    </q-page-container>
  </q-layout>
</template>

<script>
export default {
  data() {
    return {
      loginForm: {
        username: "admin",
        password: "password",
      },
    };
  },
  methods: {
    loginNotify() {
      this.$q.notify({
        message: "Login Successful",
      });
    },
    attemptLogin() {
      // Use Store Actions to login and when successful move to next page
      console.log("Attempting Login");
      console.log(this.$store);
      this.$store.dispatch("auth/login", this.loginForm).then(() => {
        console.log("Successfully logined and redirecting to new page")
        this.$router.push({ path: this.redirect || '/' })
        // this.$store.dispatch("auth/getInfo")
      }).catch((error) => {
        console.log("Login Failed error")
        console.log(error)        
      })
      // 
    },
    sendToRegister(){
      // this.$router.push({ path: '/user_register' })
    }
  },
  mounted() {
    
  }, // End of Mounted
};
</script>

<style>
#particles-js {
  position: absolute;
  width: 100%;
  height: 100%;
  background-repeat: no-repeat;
  background-size: cover;
  background-position: 50% 50%;
}
.normal_gradient {
  background: linear-gradient(145deg, rgb(74, 94, 137) 15%, #b61924 70%);
}
.dark_gradient {
  background: linear-gradient(145deg, rgb(11, 26, 61) 15%, #4c1014 70%);
}
.login-form {
  position: absolute;
}
</style>
