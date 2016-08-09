class CreateFilePositions < ActiveRecord::Migration[5.0]
  def change
    create_table :file_positions do |t|
      t.references :semantic_event, foreign_key: true
      t.string :commit_hash
      t.string :filename
      t.integer :line_number

      t.timestamps
    end
  end
end
