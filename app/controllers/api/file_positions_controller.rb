class Api::FilePositionsController < ApplicationController
  include Showable
  include Indexable
  include Createable

  private

  def parameters
    params.require(:file_position).permit(:semantic_event_id, :commit_hash, :filename, :line_number)
  end
end
