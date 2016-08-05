class CreateRepositories < ActiveRecord::Migration[5.0]
  def change
    create_table :repositories do |t|
      t.string :owner
      t.string :name
      t.string :platform

      t.timestamps
    end
    add_index :repositories, [:owner, :name, :platform], unique: true
  end
end
