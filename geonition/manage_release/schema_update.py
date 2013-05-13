schema_changes = [('master', (
    ('maps', [ 
        "ALTER TABLE maps_layer ADD COLUMN attr_title varchar(100) NOT NULL DEFAULT '';",
        "ALTER TABLE maps_layer ADD COLUMN attr_url varchar(200) NOT NULL DEFAULT '';",
        "ALTER TABLE maps_layer ADD COLUMN attr_logo_url varchar(200) NOT NULL DEFAULT '';",
        "ALTER TABLE maps_layer ADD COLUMN attr_logo_format varchar(30) NOT NULL DEFAULT '';",
        "ALTER TABLE maps_layer ADD COLUMN attr_logo_height integer;",
        "ALTER TABLE maps_layer ADD COLUMN attr_logo_width integer;",]
    ),
    ('geoforms', [
        "ALTER TABLE geoforms_questionnaire ADD COLUMN start_date date;",
        "ALTER TABLE geoforms_questionnaire ADD COLUMN end_date date;",
        "ALTER TABLE geoforms_questionnaire ADD COLUMN map varchar(50);",
        "ALTER TABLE geoforms_questionnaire ADD COLUMN description text NOT NULL DEFAULT '';",
        "ALTER TABLE geoforms_questionnaire ADD COLUMN show_detailed_areas boolean NOT NULL DEFAULT FALSE;",
        "SELECT AddGeometryColumn('geoforms_questionnaire', 'detailed_areas', (select find_srid('public', 'geoforms_questionnaire','area')), 'MULTIPOLYGON', 2);",
        "CREATE INDEX geoforms_questionnaire_detailed_areas_id ON geoforms_questionnaire USING GIST ( detailed_areas GIST_GEOMETRY_OPS );",]
    ),
    ('plan_proposals', [
        "ALTER TABLE plan_proposals_planningproject ADD COLUMN start_date date;",
        "ALTER TABLE plan_proposals_planningproject ADD COLUMN end_date date;",
        "ALTER TABLE plan_proposals_planningproject ADD COLUMN map varchar(50);",
        "ALTER TABLE plan_proposals_planningproject ADD COLUMN description text NOT NULL DEFAULT '';",
        "SELECT AddGeometryColumn('plan_proposals_planningproject', 'area', (select find_srid('public', 'geoforms_questionnaire','area')), 'POLYGON', 2);",
        "ALTER TABLE plan_proposals_planningproject ALTER area SET NOT NULL;",
        "CREATE INDEX plan_proposals_planningproject_area_id ON plan_proposals_planningproject USING GIST ( area GIST_GEOMETRY_OPS );",
]
    )
    ),
    ),
]
