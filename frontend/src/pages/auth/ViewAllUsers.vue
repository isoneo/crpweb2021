<template>
  <q-page padding class="flex flex-center">
    <!-- <q-btn label="refresh" flat dense round color="black" @click="refresh_jwt" /> -->

    <q-table
      table-header-class="bg-indigo-10 text-white"
      dense
      title="User List"
      :data="all_user_data"
      :columns="tbl_columns"
      row-key="id"
      :loading="loading"
    >
      <template v-slot:body-cell-actions="props">
        <q-td :props="props">
          <q-btn
            icon="edit"
            color="blue"
            dense
            flat
            @click="OpenUserEditDialog(props)"
          />
          <modal-user-info-edit
            ref="subuserDialog"
            :op_type="user_edit_type"
            :user_id="edit_user_id"
            @UserEditOK="resetUserId"
            @ok="resetUserId"
          />

          <q-btn
            icon="details"
            color="blue"
            dense
            flat
            @click="OpenPWDEditDialog(props)"
          />
          <modal-pwd-force-change
            ref="subPWDDialog"
            :user_id="edit_user_id"
            @UserEditOK="resetUserId"
            @ok="resetUserId"
          />
        </q-td>
      </template>
      <template v-slot:top-right>
        <q-btn
          color="primary"
          label="Create New User"
          @click="OpenCreateUser"
        />
      </template>
    </q-table>

    <!-- {{ all_user_data }} -->
  </q-page>
</template>

<script>
import { userList } from "src/api/auth";
import ModalUserInfoEdit from "src/pages/auth/dialog/DialogUserInfoEdit";
import ModalPwdForceChange from "src/pages/auth/dialog/DialogPWDForceChange";
export default {
  name: "ViewAllUsers",
  components: {
    ModalUserInfoEdit,
    ModalPwdForceChange,
  },
  data() {
    return {
      user_edit_dialog: false,
      edit_user_id: "",
      user_edit_type: "Update",
      force_pwd_dialog: false,

      all_user_data: [],
      tbl_columns: [
        { name: "email", field: "email", label: "email" },
        { field: "first_name", label: "First Name" },
        { field: "last_name", label: "Last Name" },
        { name: "role", field: (row) => row.role.name, label: "role" },
        { field: "company_id", label: "Company" },
        { field: (row) => row.department.department_name, label: "Department" },
        { name: "actions", label: "Actions", field: "", align: "center" },
      ],
      loading: false,
    };
  },
  created: function() {
    this.loadUserData();
  },
  methods: {
    loadUserData() {
      userList().then((response) => {
        console.log(response);
        this.all_user_data = response.data.users;
      });
      console.log(this.all_user_data);
    },
    OpenUserEditDialog(props) {
      console.log(props);
      var changeUserSetting = new Promise((resolve) => {
        this.user_edit_type = "Update";
        this.edit_user_id = props.row.id;
        resolve();
      });
      // this.user_edit_type = "Update"
      // this.edit_user_id = props.row.id;
      // console.log(this.$refs.subuserDialog)
      changeUserSetting.then(() => {
        this.$refs.subuserDialog.show();
      });
    },
    OpenCreateUser() {
      var changeUserSetting = new Promise((resolve) => {
        this.user_edit_type = "Create";
        resolve();
      });
      // this.user_edit_type = "Create";
      changeUserSetting.then(() => {
        this.$refs.subuserDialog.show();
      });
      // console.log(this.$refs.subuserDialog)
      // this.$refs.subuserDialog.show();
    },
    OpenPWDEditDialog(props) {
      var changeUserSetting = new Promise((resolve) => {
        this.edit_user_id = props.row.id;
        resolve();
      });
      // this.user_edit_type = "Update"
      // this.edit_user_id = props.row.id;
      // console.log(this.$refs.subuserDialog)
      changeUserSetting.then(() => {
        this.$refs.subPWDDialog.show();
      });
    },
    resetUserId($event) {
      console.log(event);
      this.edit_user_id = "";
      this.loadUserData();
    },
    refresh_jwt() {
      console.log(this.$store.getters.token);
      this.$store
        .dispatch("auth/refreshToken")
        .then(() => {
          console.log("Successfully refreshed");
          console.log(this.$store.getters.token);
          // this.$router.push({ path: this.redirect || '/' })
        })
        .catch((error) => {
          console.log("refresh failed");
          console.log(error);
        });
    },
  }, // END OF METHOD
};
</script>
