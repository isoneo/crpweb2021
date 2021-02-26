<template>
  <q-page class="q-pa-sm">
    <h4 class="text-center">Sources - Fund List</h4>
    
    <div class="q-pa-md row justify-center">
      
      <q-table
      
        :dense="$q.screen.lt.md"
        title="Fund List"
        :rows="tbl_data"
        :columns="tbl_columns"
        :loading="tbl_loading"
        row-key="ref_fund_list_id"
        v-model:pagination="tbl_pagination"
        :filter="tbl_filter"
        @request="Tblquery"
      >
        <template v-slot:top-right>
          <div class="q-pa-md q-gutter-sm row">
            <q-input
              debounce="350"
              v-model="tbl_filter"
              filled
              clearable
              dense
              color="green-8"
              placeholder="Search"
            >
              <template v-slot:append>
                <q-icon name="search" />
              </template>
            </q-input>
            <q-btn
              icon="fas fa-plus-circle"
              label="Add new record"
              @click="sw_dialog_src_fund"
            />
          </div>
        </template>
      </q-table>
    </div>
  </q-page>
</template>

<script>
import { reactive, toRefs, onMounted } from "vue";
import { useQuasar } from "quasar";

import { api_src_ref_fund_list } from "src/api/source_reference";
import DialogSrcFund from "src/pages/sources_reference/dialogs/DialogSrcFund";

export default {
  setup(props, context) {
    // Some Setup stuf
    const event = reactive({
      tbl_data: [],
      tbl_filter: "",
      tbl_columns: [
        {
          name: "ref_fund_list_id",
          align: "center",
          label: "ID",
          field: "ref_fund_list_id",
          sortable: true,
        },
        {
          name: "fund_name",
          align: "center",
          label: "Fund Name",
          field: "fund_name",
          sortable: true,
        },
        {
          name: "fund_name_descrip",
          align: "center",
          label: "Fund Description",
          field: "fund_name_descrip",
          sortable: true,
        },
      ],
      total_row: 0,
      tbl_loading: false,
      tbl_pagination: {
        sortBy: "",
        descending: false,
        page: 1,
        rowsPerPage: 5,
        rowsNumber: 0,
      },
    });
    const $q = useQuasar();
    function sw_dialog_src_fund() {
      $q.dialog({
        component: DialogSrcFund,

        // props forwarded to your custom component
        componentProps: {
          text: "something",
          // ...more..props...
        },
      })
        .onOk(() => {
          console.log("OK");
          onTblDataLoad();
        })
        .onCancel(() => {
          console.log("Cancel");
        })
        .onDismiss(() => {
          console.log("Called on OK or Cancel");
        });
    }

    function onTblDataLoad(query) {
      // console.log(props)
      event.tbl_loading = !event.tbl_loading;
      console.log(query);
      api_src_ref_fund_list(query).then((response) => {
        console.log(response);
        event.tbl_data = response.data.results;
        event.tbl_pagination.rowsNumber = response.data.count;

        // event.total_row = response.data.count;
      });
      // if (typeof query !== "undefined") {
      //   event.tbl_pagination.page = query.page;
      //   event.tbl_pagination.rowsPerPage = query.page_size;
      //   event.tbl_pagination.sortBy = query.ordering;
      // }
      console.log(event.tbl_pagination);

      event.tbl_loading = !event.tbl_loading;
    }
    function Tblquery(props) {
      const { page, rowsPerPage, sortBy, descending } = props.pagination;
      const filter = props.filter;
      console.log(props);
      // var page = info.page
      // var page_size = info.pageSize
      var sort_txt;
      var cmb_txt = {};
      sort_txt = "";

      // Setting Sort parameters
      // if (info.sort.prop !== '' & typeof info.sort.prop !== 'undefined') {
      //   if (info.sort.order === 'descending') {
      //     sort_txt = '-' + info.sort.prop.split('.').join('__')
      //   } else {
      //     sort_txt = info.sort.prop.split('.').join('__')
      //   }
      // }
      // // Fxiing Page information only if filter
      // if (info.type === 'filter') {
      //   page = 1
      // }
      // cmb_txt['project_id'] = this.main_id
      if (filter !== "" && filter !== null) {
        console.log(filter);
        cmb_txt["search"] = filter;
      }
      cmb_txt["page"] = page;
      cmb_txt["page_size"] = rowsPerPage;

      event.tbl_pagination.page = page;
      event.tbl_pagination.rowsPerPage = rowsPerPage;
      event.tbl_pagination.sortBy = sortBy;
      if (descending === true) {
        cmb_txt["ordering"] = sortBy;
      } else {
        cmb_txt["ordering"] = "-" + sortBy;
      }

      event.tbl_pagination.descending = descending;

      onTblDataLoad(cmb_txt);
    }
    function check_tbl_update(props, data) {
      console.log(data);
      console.log(props);
      console.log(event.tbl_pagination);
      const { page, rowsPerPage, sortBy, descending } = props.pagination;
      console.log(page);
      console.log(rowsPerPage);
      console.log(sortBy);
      console.log(descending);
    }
    onMounted(() => {
      onTblDataLoad({page_size:5});
      // check_tbl_update({
      //   pagination: event.tbl_pagination,
      //   filter: event.tbl_filter,
      // });
    });
    // Then return Stuff
    return {
      ...toRefs(event),
      onTblDataLoad,
      sw_dialog_src_fund,
      check_tbl_update,
      Tblquery,
    };
  },
};
</script>
