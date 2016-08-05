class CreatePullRequests < ActiveRecord::Migration[5.0]
  def change
    create_table :pull_requests do |t|
      t.references :repository, foreign_key: true
      t.integer :pull_request_number

      t.timestamps
    end
    add_index :pull_requests, [:repository_id, :pull_request_number], unique: true
  end
end
