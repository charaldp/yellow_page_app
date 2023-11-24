<template>
  <JqxDataTable :width="width" :source="dataAdapter" 
              :columns="columns" :pageSize="10" @rowDoubleClick=onContactOpen($event) :altRows="true" :pageable="true" :filterable="true">
    </JqxDataTable>
</template>

<script>
import JqxDataTable from "jqwidgets-scripts/jqwidgets-vue3/vue_jqxdatatable.vue";

export default {
  name: 'ContactsList',
  components: {
    // Adding imported widgets here
        JqxDataTable
    },
    data: function () {
        // Define properties which will use in the widget
        return {
            width: "80%",
            dataAdapter: new window.jqx.dataAdapter(this.source),
            columns: [
                { text: "id", dataField: "id", hidden: true },
                { text: 'Phone Number', cellsAlign: 'center', align: 'center', dataField: 'phone_number', width: "25%" },
                { text: 'First Name', cellsAlign: 'center', align: 'center', dataField: 'first_name', width: "25%" },
                { text: 'Last Name', cellsAlign: 'center', align: 'center', dataField: 'last_name', width: "25%" },
                { text: 'Address', cellsAlign: 'center', align: 'center', dataField: 'address', width: "25%" },
                { text: "comment", dataField: "comment", hidden: true },
            ]
        }
    },        
    beforeCreate: function () {            
        // Add here any data where you want to transform before components be rendered
        this.source = {
            dataType: 'json',
            dataFields: [
                { name: 'id', type:'number', hidden: true},
                { name: 'phone_number', type: 'string' },
                { name: 'first_name', type: 'string' },
                { name: 'last_name', type: 'string' },
                { name: 'address', type: 'string' },
                { name: 'comment', type:'string', hidden: true},
            ],
            url: 'http://localhost:8000/api/contact/?format=json',
        };
    },
    created: function() {
        this.dataAdapter = new window.jqx.dataAdapter(this.source);
    },
    methods: {
      onContactOpen(event) {
        var args = event.args;
        window.location.href = `http://localhost:8000/api/contact/${args.row.id}`;
      }
    }
}
</script>
