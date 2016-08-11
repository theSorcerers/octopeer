class Api::WindowResolutionEventsController < ApplicationController
  include Epochable
  include Showable
  include Indexable
  include Createable

  private

  def parameters
    params.require(:window_resolution_event).permit(:width, :height, :session_id, :created_at)
  end
end
