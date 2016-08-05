class CreateSessions < ActiveRecord::Migration[5.0]
  def change
    create_table :sessions do |t|
      t.references :pull_request, foreign_key: true
      t.references :user, foreign_key: true

      t.timestamps
    end
    add_index :sessions, [:pull_request_id, :user_id], unique: true
  end
end
