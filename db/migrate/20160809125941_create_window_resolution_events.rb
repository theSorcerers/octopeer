class CreateWindowResolutionEvents < ActiveRecord::Migration[5.0]
  def change
    create_table :window_resolution_events do |t|
      t.references :session, foreign_key: true
      t.integer :width
      t.integer :height

      t.timestamps
    end
  end
end
