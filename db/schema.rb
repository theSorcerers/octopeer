# This file is auto-generated from the current state of the database. Instead
# of editing this file, please use the migrations feature of Active Record to
# incrementally modify your database, and then regenerate this schema definition.
#
# Note that this schema.rb definition is the authoritative source for your
# database schema. If you need to create the application database on another
# system, you should be using db:schema:load, not running all the migrations
# from scratch. The latter is a flawed and unsustainable approach (the more migrations
# you'll amass, the slower it'll run and the greater likelihood for issues).
#
# It's strongly recommended that you check this file into your version control system.

ActiveRecord::Schema.define(version: 20160809102629) do

  # These are extensions that must be enabled in order to support this database
  enable_extension "plpgsql"

  create_table "element_types", force: :cascade do |t|
    t.string   "name"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "event_types", force: :cascade do |t|
    t.string   "name"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "file_positions", force: :cascade do |t|
    t.integer  "semantic_event_id"
    t.string   "commit_hash"
    t.string   "filename"
    t.integer  "line_number"
    t.datetime "created_at",        null: false
    t.datetime "updated_at",        null: false
    t.index ["semantic_event_id"], name: "index_file_positions_on_semantic_event_id", using: :btree
  end

  create_table "keystroke_types", force: :cascade do |t|
    t.string   "name"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
  end

  create_table "pull_requests", force: :cascade do |t|
    t.integer  "repository_id"
    t.integer  "pull_request_number"
    t.datetime "created_at",          null: false
    t.datetime "updated_at",          null: false
    t.index ["repository_id", "pull_request_number"], name: "index_pull_requests_on_repository_id_and_pull_request_number", unique: true, using: :btree
    t.index ["repository_id"], name: "index_pull_requests_on_repository_id", using: :btree
  end

  create_table "repositories", force: :cascade do |t|
    t.string   "owner"
    t.string   "name"
    t.string   "platform"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["owner", "name", "platform"], name: "index_repositories_on_owner_and_name_and_platform", unique: true, using: :btree
  end

  create_table "semantic_events", force: :cascade do |t|
    t.integer  "session_id"
    t.integer  "event_type_id"
    t.integer  "element_type_id"
    t.datetime "created_at",      null: false
    t.datetime "updated_at",      null: false
    t.index ["element_type_id"], name: "index_semantic_events_on_element_type_id", using: :btree
    t.index ["event_type_id"], name: "index_semantic_events_on_event_type_id", using: :btree
    t.index ["session_id"], name: "index_semantic_events_on_session_id", using: :btree
  end

  create_table "sessions", force: :cascade do |t|
    t.integer  "pull_request_id"
    t.integer  "user_id"
    t.datetime "created_at",      null: false
    t.datetime "updated_at",      null: false
    t.index ["pull_request_id", "user_id"], name: "index_sessions_on_pull_request_id_and_user_id", unique: true, using: :btree
    t.index ["pull_request_id"], name: "index_sessions_on_pull_request_id", using: :btree
    t.index ["user_id"], name: "index_sessions_on_user_id", using: :btree
  end

  create_table "users", force: :cascade do |t|
    t.string   "username"
    t.datetime "created_at", null: false
    t.datetime "updated_at", null: false
    t.index ["username"], name: "index_users_on_username", unique: true, using: :btree
  end

  add_foreign_key "file_positions", "semantic_events"
  add_foreign_key "pull_requests", "repositories"
  add_foreign_key "semantic_events", "element_types"
  add_foreign_key "semantic_events", "event_types"
  add_foreign_key "semantic_events", "sessions"
  add_foreign_key "sessions", "pull_requests"
  add_foreign_key "sessions", "users"
end
